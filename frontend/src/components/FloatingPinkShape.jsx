import React from 'react';

const FloatingPinkShape = ({ className }) => {
  return (
    <div
      className={className}
      style={{
        backgroundColor: 'rgba(236, 64, 122, 0.3)', // soft pink
        width: '260px',
        height: '260px',
        borderRadius: '50%',
        filter: 'blur(80px)',
        position: 'absolute',
        top: '30px',
        left: '-100px',
        pointerEvents: 'none',
        userSelect: 'none',
        zIndex: 1,
      }}
    ></div>
  );
};

export default FloatingPinkShape;
