//----------------------------------------------------------------
// #Icons
import { FaPython, FaReact, FaUikit, FaBootstrap, FaNode, FaSass, FaWindows} from "react-icons/fa";
import { IoLogoJavascript} from "react-icons/io";
import { SiPowershell, SiFlask, SiPostgresql, SiDjango, SiPostman, SiExpress} from "react-icons/si";
//----------------------------------------------------------------

function About() {
    return (
      <div className="about-container"> 
      <div className="languages-container">
        Languages :
        <IoLogoJavascript className="about-icon"/>
        <FaPython className="about-icon"/> 
        </div>
        <div className="frontend-container">
          Frontend :
            <FaReact className="about-icon" />
            <FaSass className="about-icon"/>
            <FaUikit className="about-icon"/>
            <FaBootstrap className="about-icon"/>
          </div>
        <div className="api-container">
          Api :
              <SiExpress className="about-icon"/>
              <SiFlask className="about-icon"/>
              <SiDjango className="about-icon"/>
              <SiPostman className="about-icon"/>
          </div>
        <div className="backend-container">
              Backend :
              <SiPostgresql className="about-icon"/>
              <FaNode className="about-icon"/>
              <SiPowershell className="about-icon"/>
              <FaWindows className="about-icon"/>
          </div>
      </div>
    );
  }
  
  export default About;