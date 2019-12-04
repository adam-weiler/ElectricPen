// Vanilla React:
import React from 'react';

// Image files:
import electric_pen_logo from './Img/ElectricPen-logo.png';

// Call stylesheet last:
import './Header.css';

const Header = () => {
  return (
    <header>
      <div className='logo'>
        <img src={electric_pen_logo} border='0' alt='ElectricPen logo' />
        <div className='float-right'>
          <h1 className='text-center'>ElectricPen</h1>
          <p>Helpful Digital Blog</p>
        </div>
      </div>
    </header>
  );
};

export default Header;
