import requests
import sys
import json
from datetime import datetime

class AlumniNetworkAPITester:
    def __init__(self, base_url="https://unialumni-net.preview.emergentagent.com"):
        self.base_url = base_url
        self.token = None
        self.user_id = None
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def log_test(self, name, success, details=""):
        """Log test result"""
        self.tests_run += 1
        if success:
            self.tests_passed += 1
            print(f"✅ {name} - PASSED")
        else:
            print(f"❌ {name} - FAILED: {details}")
        
        self.test_results.append({
            "test": name,
            "success": success,
            "details": details
        })

    def run_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        test_headers = {'Content-Type': 'application/json'}
        
        if self.token:
            test_headers['Authorization'] = f'Bearer {self.token}'
        
        if headers:
            test_headers.update(headers)

        try:
            if method == 'GET':
                response = requests.get(url, headers=test_headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=test_headers)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=test_headers)

            success = response.status_code == expected_status
            details = f"Status: {response.status_code}"
            
            if not success:
                try:
                    error_data = response.json()
                    details += f", Response: {error_data}"
                except:
                    details += f", Response: {response.text[:200]}"
            
            self.log_test(name, success, details)
            
            if success:
                try:
                    return True, response.json()
                except:
                    return True, {}
            else:
                return False, {}

        except Exception as e:
            self.log_test(name, False, f"Exception: {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test root API endpoint"""
        return self.run_test("Root API", "GET", "api/", 200)

    def test_user_registration(self):
        """Test user registration"""
        test_user_data = {
            "full_name": "Test User Alumni",
            "email": f"test_user_{datetime.now().strftime('%H%M%S')}@test.com",
            "password": "TestPass123!",
            "passout_year": 2020,
            "current_location": "San Francisco, CA",
            "current_company": "Tech Corp",
            "domain": "Software Engineering",
            "phone": "(555) 123-4567"
        }
        
        success, response = self.run_test(
            "User Registration",
            "POST",
            "api/auth/register",
            200,
            data=test_user_data
        )
        
        if success and 'token' in response:
            self.token = response['token']
            self.user_id = response['user']['id']
            return True
        return False

    def test_user_login(self):
        """Test user login with existing credentials"""
        # First register a user for login test
        test_email = f"login_test_{datetime.now().strftime('%H%M%S')}@test.com"
        reg_data = {
            "full_name": "Login Test User",
            "email": test_email,
            "password": "LoginTest123!",
            "passout_year": 2019,
            "current_location": "New York, NY",
            "current_company": "Login Corp",
            "domain": "Testing",
            "phone": "(555) 987-6543"
        }
        
        # Register user first
        reg_success, reg_response = self.run_test(
            "Registration for Login Test",
            "POST",
            "api/auth/register",
            200,
            data=reg_data
        )
        
        if not reg_success:
            return False
        
        # Now test login
        login_data = {
            "email": test_email,
            "password": "LoginTest123!"
        }
        
        success, response = self.run_test(
            "User Login",
            "POST",
            "api/auth/login",
            200,
            data=login_data
        )
        
        return success and 'token' in response

    def test_dashboard_stats(self):
        """Test dashboard stats endpoint"""
        return self.run_test("Dashboard Stats", "GET", "api/dashboard/stats", 200)

    def test_get_events(self):
        """Test get events endpoint"""
        success, response = self.run_test("Get Events", "GET", "api/events", 200)
        
        if success and isinstance(response, list) and len(response) == 10:
            self.log_test("Events Count Validation", True, f"Found {len(response)} events")
            return True
        elif success:
            self.log_test("Events Count Validation", False, f"Expected 10 events, got {len(response) if isinstance(response, list) else 'invalid response'}")
        
        return success

    def test_user_profile(self):
        """Test get user profile"""
        if not self.token:
            self.log_test("User Profile", False, "No authentication token")
            return False
        
        return self.run_test("Get User Profile", "GET", "api/user/profile", 200)

    def test_user_search(self):
        """Test user search functionality"""
        if not self.token:
            self.log_test("User Search", False, "No authentication token")
            return False
        
        return self.run_test("User Search", "GET", "api/users/search?q=test", 200)

    def test_event_registration(self):
        """Test event registration"""
        if not self.token:
            self.log_test("Event Registration", False, "No authentication token")
            return False
        
        # First get events to find one with registration
        events_success, events_response = self.run_test("Get Events for Registration", "GET", "api/events", 200)
        
        if not events_success or not isinstance(events_response, list):
            return False
        
        # Find an event with registration enabled
        registration_event = None
        for event in events_response:
            if event.get('has_registration'):
                registration_event = event
                break
        
        if not registration_event:
            self.log_test("Event Registration", False, "No events with registration found")
            return False
        
        reg_data = {
            "name": "Test Registration User",
            "email": "test_reg@test.com",
            "phone": "(555) 111-2222",
            "attend_dinner": True
        }
        
        return self.run_test(
            "Event Registration",
            "POST",
            f"api/events/{registration_event['id']}/register",
            200,
            data=reg_data
        )

    def test_donation(self):
        """Test donation functionality"""
        if not self.token:
            self.log_test("Donation", False, "No authentication token")
            return False
        
        donation_data = {
            "name": "Test Donor",
            "email": "donor@test.com",
            "phone": "(555) 333-4444",
            "amount": 100.0,
            "purpose": "Test Donation",
            "message": "This is a test donation"
        }
        
        return self.run_test("Donation", "POST", "api/donations", 200, data=donation_data)

    def test_feedback(self):
        """Test feedback submission"""
        feedback_data = {
            "message": "This is a test feedback message for the alumni network platform."
        }
        
        return self.run_test("Feedback Submission", "POST", "api/feedback", 200, data=feedback_data)

    def test_phone_validation(self):
        """Test phone number validation"""
        # Test invalid phone format
        invalid_user_data = {
            "full_name": "Invalid Phone User",
            "email": f"invalid_phone_{datetime.now().strftime('%H%M%S')}@test.com",
            "password": "TestPass123!",
            "passout_year": 2021,
            "current_location": "Test City",
            "current_company": "Test Company",
            "domain": "Testing",
            "phone": "555-123-4567"  # Invalid format (should be (XXX) XXX-XXXX)
        }
        
        success, response = self.run_test(
            "Phone Validation (Invalid Format)",
            "POST",
            "api/auth/register",
            422,  # Expecting validation error
            data=invalid_user_data
        )
        
        return success  # Success means it properly rejected invalid phone

    def test_profile_update(self):
        """Test profile update functionality"""
        if not self.token:
            self.log_test("Profile Update", False, "No authentication token")
            return False
        
        update_data = {
            "full_name": "Updated Test User",
            "current_location": "Updated Location",
            "phone": "(555) 999-8888"
        }
        
        return self.run_test("Profile Update", "PUT", "api/user/profile", 200, data=update_data)

    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting Global Horizon Alumni Network API Tests")
        print("=" * 60)
        
        # Basic API tests
        self.test_root_endpoint()
        
        # Authentication tests
        self.test_user_registration()
        self.test_user_login()
        
        # Phone validation test
        self.test_phone_validation()
        
        # Dashboard and events
        self.test_dashboard_stats()
        self.test_get_events()
        
        # User profile tests (requires authentication)
        self.test_user_profile()
        self.test_profile_update()
        
        # Search functionality
        self.test_user_search()
        
        # Event registration
        self.test_event_registration()
        
        # Donation functionality
        self.test_donation()
        
        # Feedback
        self.test_feedback()
        
        # Print summary
        print("\n" + "=" * 60)
        print(f"📊 Test Summary: {self.tests_passed}/{self.tests_run} tests passed")
        
        if self.tests_passed == self.tests_run:
            print("🎉 All tests passed!")
            return 0
        else:
            print(f"⚠️  {self.tests_run - self.tests_passed} tests failed")
            return 1

def main():
    tester = AlumniNetworkAPITester()
    return tester.run_all_tests()

if __name__ == "__main__":
    sys.exit(main())