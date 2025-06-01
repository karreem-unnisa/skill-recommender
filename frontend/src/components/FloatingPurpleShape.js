// FloatingPurpleShape.js
import React from 'react';

export default function FloatingPurpleShape() {
  return (
    <svg width="180" height="180" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg" style={{filter: 'blur(60px)', opacity: 0.15, borderRadius: '50%'}}>
      <circle cx="90" cy="90" r="90" fill="#9c27b0" />
    </svg>
  );
}
