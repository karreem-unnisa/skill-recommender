import React, { useState } from 'react';
import axios from 'axios';
import './Home.css'; // Use this for styling
import headerImage from '../assets/header.jpg';

const Home = () => {
  const [skills, setSkills] = useState('');
  const [numberOfRecs, setNumberOfRecs] = useState(3);
  const [mode, setMode] = useState('recommend');
  const [results, setResults] = useState([]);
  const [bonus, setBonus] = useState([]);
  const [noMatch, setNoMatch] = useState(false);

  const getRandomSubset = (array, n) => {
    if (n >= array.length) return array;
    const shuffled = [...array].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, n);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setNoMatch(false);
    setResults([]);
    setBonus([]);

    const skillArray = skills.split(',').map(s => s.trim()).filter(s => s.length > 0);

    if (skillArray.length === 0) {
      setNoMatch(true);
      return;
    }

    try {
      if (mode === 'recommend') {
        const res = await axios.post(`${BASE_URL}/api/recommend`, { skills: skillArray });
        const allResults = res.data.recommendations || [];
        if (allResults.length === 0) {
          setNoMatch(true);
        } else {
          setResults(getRandomSubset(allResults, numberOfRecs));
        }
      } else if (mode === 'learn') {
        const res = await axios.post(`${BASE_URL}/api/learn`, {
          skills: skillArray,
          limit: numberOfRecs
        });
        const learnResults = res.data.recommendations || [];
        const bonusIdeas = res.data.bonus_business_ideas || [];

        if (learnResults.length === 0) {
          setNoMatch(true);
        } else {
          setResults(learnResults);
          setBonus(bonusIdeas);
        }
      }
    } catch (err) {
      console.error('Error fetching data:', err);
      setNoMatch(true);
    }
  };

  return (
    <div className="home-container">
      {/* Full-width header image */}
      <div className="header-image-container">
        <img
           src={headerImage}
          alt="Inspiring business women"
          className="header-image"
        />
      </div>

      {/* Intro text and mentorship offer */}
      <section className="intro-section">
        <h2>How Our Recommendation System Helps You</h2>
        <p>
          Discover business ideas or learning resources tailored just for your unique skill set.
          Get inspired and empowered to start your journey with actionable recommendations.
        </p>
        <p className="mentorship-ask">
          Need mentorship to kick-start your business?{' '}
          <a href="/contact" className="mentorship-link">Reach out to us!</a>
        </p>
      </section>

      {/* Main content: form + results side by side */}
      <section className="main-content">
        <form className="recommender-form" onSubmit={handleSubmit}>
          <select value={mode} onChange={(e) => setMode(e.target.value)} aria-label="Select recommendation mode">
            <option value="recommend">Business Idea</option>
            <option value="learn">Learning Resources</option>
          </select>

          <input
            type="text"
            placeholder="Enter skills (e.g., stitching, baking)"
            value={skills}
            onChange={(e) => setSkills(e.target.value)}
            required
            aria-label="Input skills separated by comma"
          />

          <input
            type="number"
            min="1"
            placeholder="Number of Results"
            value={numberOfRecs}
            onChange={(e) => setNumberOfRecs(Number(e.target.value))}
            required
            aria-label="Number of results to display"
          />

          <button type="submit">Get Results</button>
        </form>

        <div className="results-container">
          {noMatch && (
            <div className="no-match-message">
              No matches found. Please check for typos or try alternate terms.
            </div>
          )}

          {/* Business Recommendations */}
          {mode === 'recommend' && results.length > 0 && (
            <>
              <h3>Business Recommendations:</h3>
              {results.map((rec, idx) => (
                <div key={idx} className="card">
                  <h4>{rec.business_idea}</h4>
                  <p><strong>Matched Skills:</strong> {Array.isArray(rec.matched_skills) ? rec.matched_skills.join(', ') : 'N/A'}</p>
                  <p><strong>Business Type:</strong> {rec.business_type}</p>
                  <p><strong>Tools Needed:</strong> {rec.tools_needed}</p>
                  <p><strong>Initial Investment:</strong> ₹{rec.initial_investment}</p>
                  <p><strong>Monthly Income:</strong> ₹{rec.monthly_income}</p>
                  <p><strong>Getting Started Plan:</strong> {rec.getting_started_plan}</p>
                  <p><strong>Growth Plan:</strong> {rec.growth_plan}</p>
                  <p><strong>Tips:</strong> {rec.tips}</p>
                  <p><strong>Learning Resources:</strong> {rec.learning_resources}</p>
                </div>
              ))}
            </>
          )}

          {/* Learning Resources */}
          {mode === 'learn' && results.length > 0 && (
            <>
              <h3>Learning Resources:</h3>
              {results.map((rec, idx) => (
                <div key={idx} className="card">
                  <h4>{rec.resource_name}</h4>
                  <p><strong>Platform:</strong> {rec.platform}</p>
                  <p><strong>Skill:</strong> {rec.skill_name}</p>
                  <p><strong>Difficulty:</strong> {rec.skill_level}</p>
                  <p><strong>Type:</strong> {rec.resource_type}</p>
                  <p><strong>Cost:</strong> {rec.cost}</p>
                  <p><strong>Duration:</strong> {rec.duration}</p>
                  <p><strong>Earning Potential After Learning:</strong> {rec.earning_potential_after_learning}</p>
                </div>
              ))}

              {bonus.length > 0 && (
                <>
                  <h3>Business you can start After Learning:</h3>
                  {bonus.map((b, i) => (
                    <div key={i} className="card">
                      <h4>{b.business_idea}</h4>
                      <p><strong>Matched Skills:</strong> {Array.isArray(b.matched_skills) ? b.matched_skills.join(', ') : 'N/A'}</p>
                      <p><strong>Monthly Income:</strong> ₹{b.monthly_income}</p>
                      <p><strong>Initial Investment:</strong> ₹{b.initial_investment}</p>
                      <p><strong>And Many More...</strong></p>
                      <p>You also get business ideas by choosing "Business Idea" from the dropdown above.</p>
                    </div>
                  ))}
                </>
              )}
            </>
          )}
        </div>
      </section>
    </div>
  );
};

export default Home;
