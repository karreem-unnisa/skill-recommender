import React from 'react';
import { useNavigate } from 'react-router-dom';
import './LandingPage.css';
import landingImage from '../assets/image.png'; 
import { ReactComponent as HowIllustration } from '../assets/how-illustration.svg';
import { ReactComponent as WhyIllustration } from '../assets/why-illustration.svg';
import FloatingPinkShape from '../components/FloatingPinkShape';
import FloatingPurpleShape from '../components/FloatingPurpleShape';

const LandingPage = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate('/home');  // Redirect to your Home.js route
  };

  return (
    <div className="landing-container">
      <div className="left-half" style={{ position: 'relative' }}>
        {/* Floating decorative shapes */}
        <FloatingPinkShape className="floating-shape pink" />
        <FloatingPurpleShape className="floating-shape purple" />

        <header className="landing-header" data-aos="fade-up">
          <h1>Empower Your Skills</h1>
          <p className="tagline">
            Transform your abilities into opportunities. Discover personalized business ideas and learning paths tailored just for you.
          </p>
          <button onClick={handleGetStarted} className="btn-get-started">
            Get Started
          </button>
        </header>

        <section className="how-it-works" data-aos="fade-up" data-aos-delay="100">
          <h2>How It Works</h2>
          <HowIllustration className="decor-illustration" />
          <ul>
            <li><strong>1.</strong> Select your skills or interests</li>
            <li><strong>2.</strong> Get personalized business ideas and learning resources</li>
            <li><strong>3.</strong> Plan your journey and start growing</li>
          </ul>
        </section>

        <section className="why-us" data-aos="fade-up" data-aos-delay="200">
          <h2>Why Choose Us?</h2>
          <WhyIllustration className="decor-illustration" />
          <p>
            We focus on women empowerment by providing a unique, skill-based recommendation system with curated resources and actionable business ideas.
          </p>
        </section>
      </div>

      <div className="right-half">
        <img src={landingImage} alt="Empower Your Skills" />
      </div>
    </div>
  );
};

export default LandingPage;
