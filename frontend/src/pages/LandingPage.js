import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';

const LandingPage = () => {
  const navigate = useNavigate();

  return (
    <div className="landing-page">
      {/* Navbar */}
      <nav className="navbar">
        <div className="logo">🌸 SkillBridge</div>
       
      </nav>

      {/* Hero */}
      <section className="hero">
        <p className="badge">🌟 Empowering Women Entrepreneurs</p>
        <h1>
          Transform Your Skills Into <span className="highlight">Financial Freedom</span>
        </h1>
        <p className="subtext">
          Discover personalized business opportunities or learning paths tailored to your unique skills.
          Our AI-powered platform helps homemakers build successful businesses and achieve financial independence.
        </p>
        <div className="cta-buttons">
          <button onClick={() => navigate('/home')} className="btn primary">Get Started Free →</button>
         
        </div>
        <div className="trust-stats">
          <span>👩‍🦰 10,000+ Women Empowered</span>
          <span>✅ 95% Success Rate</span>
          <span>📈 ₹50L+ Revenue Generated</span>
        </div>
      </section>

      {/* How It Works */}
      <section className="how-section">
        <h2>How SkillBridge Works</h2>
        <p className="section-sub">Our intelligent platform analyzes your skills and preferences to provide personalized recommendations</p>
        <div className="cards">
          <div className="card">
            <div className="icon">🔍</div>
            <h3>Skill Assessment</h3>
            <p>Tell us about your existing skills, interests, and goals. Our system evaluates your strengths and potential.</p>
          </div>
          <div className="card">
            <div className="icon">🧠</div>
            <h3>AI Recommendations</h3>
            <p>Get personalized business ideas or learning paths powered by machine learning and market analysis.</p>
          </div>
          <div className="card">
            <div className="icon">🚀</div>
            <h3>Take Action</h3>
            <p>Follow detailed guides and step-by-step plans to launch your business or begin your learning journey.</p>
          </div>
        </div>
      </section>

      {/* Gradient CTA */}
      <footer className="cta-footer">
        <h2>Ready to Start Your Journey?</h2>
        <p>Join thousands of women who have transformed their lives through SkillBridge</p>
        <button className="btn light" onClick={() => navigate('/home')}>Start Your Assessment →</button>
      </footer>
    </div>
  );
};

export default LandingPage;
