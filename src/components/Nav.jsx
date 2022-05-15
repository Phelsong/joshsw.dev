import {Link} from 'react-router-dom'


function Nav() {
    return (
      <div className="nav-container"> 
      <Link to="/">About</Link>
      <Link to="/about">About</Link>
      <Link to="/Projects">Projects</Link>
      </div>
    );
  }
  
  export default Nav;