import { Link } from "react-router-dom";

//----------------------------------------------------------------
function Nav() {
  return (
    <div className="nav-container">
      <Link to="/about" uk-icon="info" className="nav-icon"></Link>
      <div className="nav-logo-container">
        <h3 className="main-title">Josh S Wilkinson</h3>
      </div>
      <Link to="/Projects" uk-icon="code" className="nav-icon"></Link>
    </div>
  );
}
//----------------------------------------------------------------
export default Nav;
