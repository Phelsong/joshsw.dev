import {Link} from 'react-router-dom'

//----------------------------------------------------------------
function Nav() {
    return (
      <div className="nav-container"> 
      <Link to="/about" uk-icon="info"></Link>
      <img src="../Assets/JwilkDevLogo.svg" alt="logo"/>
      <h3>Josh S Wilkinson</h3>
      <Link to="/Projects" uk-icon="code"></Link>
      </div>
    );
  }
//----------------------------------------------------------------
  export default Nav;