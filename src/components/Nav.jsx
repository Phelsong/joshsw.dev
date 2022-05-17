import { Link } from "react-router-dom";

//----------------------------------------------------------------
function Nav() {
  return (
    <div className="nav-container">
      <Link to="/about" uk-icon="info"></Link>
      <div className="nav-logo-container">
        <svg src={require("../Assets/JwilkDevLogo.svg")} alt="logo"/>
        <h3>Josh S Wilkinson</h3>
      </div>
      <Link to="/Projects" uk-icon="code"></Link>
    </div>
  );
}
//----------------------------------------------------------------
export default Nav;
