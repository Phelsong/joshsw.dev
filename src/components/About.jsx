//----------------------------------------------------------------
// #Icons
import {
  FaPython,
  FaReact,
  FaUikit,
  FaBootstrap,
  FaNode,
  FaSass,
} from "react-icons/fa";
import { IoLogoJavascript } from "react-icons/io";
import {
  SiPowershell,
  SiFlask,
  SiPostgresql,
  SiDjango,
  SiPostman,
  SiExpress,
} from "react-icons/si";
import "../Assets/BeekeeperLogopng.png"
//----------------------------------------------------------------

function About() {
  return (
    <div className="about-container">
      <div className="languages-container">
      <h5 className="about-title"> Main Languages : </h5>
      <span className="tech-sub-container">
        <IoLogoJavascript className="about-icon" />
        JavaScript
        </span>
        <span className="tech-sub-container">
        <FaPython className="about-icon" />
        Python
        </span>
      </div>
      {/* languages ends ^^^^^^^^^^^^^ */}
      <div className="tech-container">
        <div className="frontend-container">
          <h5 className="about-title"> Frontend : </h5>
          <span className="tech-sub-container">
          <FaReact className="about-icon" />
          React
          </span>
          <span className="tech-sub-container">
          <FaSass className="about-icon" />
          Sass
          </span>
          <span className="tech-sub-container">
          <FaUikit className="about-icon" />
          UiKit
          </span>
          <span className="tech-sub-container">
          <FaBootstrap className="about-icon" />
          Bootstrap
          </span>
        </div>
        {/* FrontEnd Ends ^^^^^^^^^^^^^^^^^^^^ */}
        <div className="api-container">
          <h5 className="about-title"> Api : </h5>
          <span className="tech-sub-container">
          <SiExpress className="about-icon" />
          Express
          </span> 
          <span className="tech-sub-container">
          <SiFlask className="about-icon" />
          Flask
          </span>
          <span className="tech-sub-container">
          <SiDjango className="about-icon" />
          Django
          </span>
          <span className="tech-sub-container">
          <SiPostman className="about-icon" />
          Postman
          </span>
        </div>
        {/* API ends ^^^^^^^^^^^^^^^^^^ */}
        {/* Backend Start ************ */}
        <div className="backend-container">
          <h5 className="about-title"> Backend :</h5>
          <span className="tech-sub-container">
          <SiPostgresql className="about-icon" />
          PostgreSql
          </span>
          <span className="tech-sub-container">
          <FaNode className="about-icon" />
          Node
          </span>
          <span className="tech-sub-container">
          <SiPowershell className="about-icon" />
          PowerShell
          </span>
          <span className="tech-sub-container">
          <svg src={require("../Assets/BeekeeperLogo.svg")} alt="beekeeper" className="about-icon"/>
            Beekeeper 
            </span>
        </div>
        {/* Backend ends ^^^^^^^^^^^^^^ */}
      </div>
    </div>
  );
}

export default About;
