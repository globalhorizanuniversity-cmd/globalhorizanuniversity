import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Button } from '@/components/ui/button';
import { Home, Calendar, MessageCircle, Heart, Info, Mail, User, LogOut, Menu, X } from 'lucide-react';
import { toast } from 'sonner';

const Layout = ({ children, user, setUser }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    setUser(null);
    toast.success('Logged out successfully');
    navigate('/');
  };

  const menuItems = [
    { icon: Home, label: 'Home', path: '/dashboard', testId: 'sidebar-home' },
    { icon: Calendar, label: 'Events', path: '/events', testId: 'sidebar-events' },
    { icon: MessageCircle, label: 'Connect', path: '/connect', testId: 'sidebar-connect' },
    { icon: Heart, label: 'Donate', path: '/donate', testId: 'sidebar-donate' },
    { icon: Info, label: 'About', path: '/about', testId: 'sidebar-about' },
    { icon: Mail, label: 'Contact', path: '/contact', testId: 'sidebar-contact' },
    { icon: User, label: 'Profile', path: '/profile', testId: 'sidebar-profile' }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-purple-50 to-orange-50">
      {/* Mobile Menu Button */}
      <button
        onClick={() => setSidebarOpen(!sidebarOpen)}
        className="lg:hidden fixed top-4 left-4 z-50 bg-white p-3 rounded-full shadow-lg"
        data-testid="mobile-menu-toggle"
      >
        {sidebarOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
      </button>

      {/* Sidebar */}
      <aside
        className={`fixed top-0 left-0 h-full bg-gradient-to-b from-blue-900 to-purple-900 text-white w-64 transform transition-transform duration-300 ease-in-out z-40 ${
          sidebarOpen ? 'translate-x-0' : '-translate-x-full'
        } lg:translate-x-0`}
        data-testid="sidebar"
      >
        <div className="p-6">
          <div className="flex items-center gap-3 mb-8">
            <img
              src="https://images.unsplash.com/photo-1583373834259-46cc92173cb7"
              alt="Logo"
              className="w-12 h-12 rounded-full"
            />
            <div>
              <h2 className="font-bold text-lg">Global Horizon</h2>
              <p className="text-xs text-blue-200">Alumni Network</p>
            </div>
          </div>

          <nav className="space-y-2">
            {menuItems.map((item) => (
              <button
                key={item.path}
                onClick={() => {
                  navigate(item.path);
                  setSidebarOpen(false);
                }}
                className={`w-full flex items-center gap-3 px-4 py-3 rounded-lg transition-colors ${
                  location.pathname === item.path
                    ? 'bg-white text-blue-900'
                    : 'hover:bg-white/10'
                }`}
                data-testid={item.testId}
              >
                <item.icon className="w-5 h-5" />
                <span className="font-medium">{item.label}</span>
              </button>
            ))}

            <button
              onClick={handleLogout}
              className="w-full flex items-center gap-3 px-4 py-3 rounded-lg hover:bg-red-500/20 transition-colors text-red-300 hover:text-red-200"
              data-testid="sidebar-logout"
            >
              <LogOut className="w-5 h-5" />
              <span className="font-medium">Logout</span>
            </button>
          </nav>
        </div>
      </aside>

      {/* Main Content */}
      <main className="lg:ml-64 min-h-screen">
        {children}
      </main>

      {/* Overlay for mobile */}
      {sidebarOpen && (
        <div
          className="lg:hidden fixed inset-0 bg-black/50 z-30"
          onClick={() => setSidebarOpen(false)}
        ></div>
      )}
    </div>
  );
};

export default Layout;