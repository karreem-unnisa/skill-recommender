import React, { useState } from 'react';
import axios from 'axios';
import './Home.css';
import { BASE_URL } from '../config';
import { Link } from 'react-router-dom';


const Home = () => {
  const [step, setStep] = useState(1);
  const [skills, setSkills] = useState('');
  const [mode, setMode] = useState('recommend');
  const [numberOfRecs, setNumberOfRecs] = useState(5);
  const [results, setResults] = useState([]);
  const [bonus, setBonus] = useState([]);
 
  const [noMatch, setNoMatch] = useState(false);

  const getRandomSubset = (array, n) => {
    if (n >= array.length) return array;
    const shuffled = [...array].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, n);
  };

  const handleRecommendation = async () => {
    const skillArray = skills.split(',').map(s => s.trim()).filter(Boolean);
    if (skillArray.length === 0) {
      setNoMatch(true);
      return;
    }

   
    setNoMatch(false);
    setResults([]);
    setBonus([]);

    try {
      if (mode === 'recommend') {
        const res = await axios.post(`${BASE_URL}/api/recommend`, { skills: skillArray });
        const allResults = res.data.recommendations || [];
        if (allResults.length === 0) setNoMatch(true);
        else setResults(getRandomSubset(allResults, numberOfRecs));
      } else {
        const res = await axios.post(`${BASE_URL}/api/learn`, { skills: skillArray, limit: numberOfRecs });
        const learnResults = res.data.recommendations || [];
        const bonusIdeas = res.data.bonus_business_ideas || [];
        if (learnResults.length === 0) setNoMatch(true);
        else {
          setResults(learnResults);
          setBonus(bonusIdeas);
        }
      }
    } catch (err) {
      console.error('Error:', err);
      setNoMatch(true);
    }

    setStep(4);
  };

  return (
    <div className="home-container">
      <nav className="navbar">
  <Link to="/" className="logo">🌸 SkillBridge</Link>
</nav>

      <div className="step-indicator">Step {step} of 4</div>

      {/* Step 1 */}
      {step === 1 && (
        <section className="step-section">
          <h2>✨ Let's Start with Your Skills</h2>
          <input
            type="text"
            placeholder="e.g., cooking, teaching, gardening"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
          />
          <button onClick={() => setStep(2)}>Next →</button>
        </section>
      )}

      {/* Step 2 */}
      {step === 2 && (
        <section className="step-section">
          <h2>🛤️ What Would You Like to Explore?</h2>
          <div className="option-cards">
            <div className={`option-card ${mode === 'recommend' ? 'active' : ''}`} onClick={() => setMode('recommend')}>
              <h3>💡 Business Ideas</h3>
              <p>Get startup ideas matched to your skills</p>
            </div>
            <div className={`option-card ${mode === 'learn' ? 'active' : ''}`} onClick={() => setMode('learn')}>
              <h3>📚 Learning Paths</h3>
              <p>Learn new skills with earning potential</p>
            </div>
          </div>

          <label>🔢 How many recommendations?</label>
          <div className="rec-counts">
            {[3, 5, 7, 10].map(n => (
              <button key={n} className={numberOfRecs === n ? 'selected' : ''} onClick={() => setNumberOfRecs(n)}>
                {n}
              </button>
            ))}
          </div>

          <button onClick={() => { setStep(3); handleRecommendation(); }}>
            🚀 Get My Recommendations
          </button>
        </section>
      )}

      {/* Step 3 */}
      {step === 3 && (
        <section className="step-section loading">
          <h2>🧠 Analyzing your skills...</h2>
          <p>AI is generating the best paths for you. Hang tight!</p>
          <div className="spinner"></div>
        </section>
      )}

      {/* Step 4 */}
      {step === 4 && (
        <section className="results-section">
          {noMatch ? (
            <div className="no-match">❌ No matches found. Try again.</div>
          ) : (
            <>
              <h2>{mode === 'recommend' ? '🚀 Business Ideas for You' : '📚 Learn & Grow'}</h2>
              <div className="result-blocks">
                {results.map((rec, idx) => (
                  <div className="result-wrapper" key={idx}>
                    <div className="result-title-card">
                      {mode === 'recommend' ? `💡 ${rec.business_idea}` : `📘 ${rec.resource_name}`}
                    </div>
                    <div className="feature-grid">
                      {mode === 'recommend' ? (
                        <>
                          <div className="feature-card">📂 <strong>Type:</strong> {rec.business_type}</div>
                          <div className="feature-card">🎯 <strong>Skills:</strong> {rec.matched_skills?.join(', ')}</div>
                          <div className="feature-card">🛠️ <strong>Tools:</strong> {rec.tools_needed}</div>
                          <div className="feature-card">💸 <strong>Investment:</strong> ₹{rec.initial_investment}</div>
                          <div className="feature-card">📈 <strong>Monthly Income:</strong> ₹{rec.monthly_income}</div>
                          <div className="feature-card">🚀 <strong>Getting Started:</strong> {rec.getting_started_plan}</div>
                          <div className="feature-card">🌱 <strong>Growth Plan:</strong> {rec.growth_plan}</div>
                        </>
                      ) : (
                        <>
                          <div className="feature-card">🖥️ <strong>Platform:</strong> {rec.platform}</div>
                          <div className="feature-card">🎯 <strong>Skill:</strong> {rec.skill_name}</div>
                          <div className="feature-card">📊 <strong>Difficulty:</strong> {rec.skill_level}</div>
                          <div className="feature-card">💰 <strong>Cost:</strong> ₹{rec.cost}</div>
                          <div className="feature-card">⏳ <strong>Duration:</strong> {rec.duration}</div>
                          <div className="feature-card">📈 <strong>Income Potential:</strong> {rec.earning_potential_after_learning}</div>
                        </>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </>
          )}

          {/* Bonus */}
          {mode === 'learn' && bonus.length > 0 && (
            <div className="bonus-section">
              <h3>✨ Bonus Business Ideas</h3>
              <div className="result-blocks">
                {bonus.map((b, i) => (
                  <div className="result-wrapper" key={i}>
                    <div className="result-title-card">🌟 {b.business_idea}</div>
                    <div className="feature-grid">
                      <div className="feature-card">🎯 <strong>Skills:</strong> {b.matched_skills?.join(', ')}</div>
                      <div className="feature-card">💸 <strong>Income:</strong> ₹{b.monthly_income}</div>
                      <div className="feature-card">🪙 <strong>Investment:</strong> ₹{b.initial_investment}</div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          <button className="start-over-btn" onClick={() => window.location.reload()}>🔁 Start Over</button>
        </section>
      )}
    </div>
  );
};

export default Home;
