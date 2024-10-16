import './SideBar.css';

function SideBar() {

    return (
        <div className="SideBar" >
            <div className='ProfileImage'><img src='https://loginext-media-bucket.s3-ap-southeast-1.amazonaws.com/images/loginext-logos-icons/reportredirection/ReportLinkFailed2.png' alt='Photo' /></div>
            <div className='Name'> Ankush Saini </div>
            <div className='Name'> DevOps Engineer </div>

            <div>
                <ul>
                    <li>HOME</li>
                    <li>ABOUT</li>
                    <li>SKILLS</li>
                    <li>EDUCATION</li>
                    <li>EXPERIENCE</li>
                    <li>PROJECTS</li>
                    <li>CONTACT</li>
                </ul>
            </div>

            <div> © copyright 2024 All rights reserved.</div>
            <div>Made with by Ankush</div>
        </div>
    );
}

export default SideBar;