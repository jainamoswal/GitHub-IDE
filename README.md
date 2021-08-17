## What is this ? 

**This is an IDE running on GitHub Actions which can help in.....**
1. Running small snippets.
2. Running codes whenever PC is not available and setting python on mobile is pain in ass.
3. Copy pasting in proper indentations which is harder while using Mobile to code.
4. Showing code executions to public/Sharing them online.
5. Have a greate collection of snippets for duture use.
6. Testing codes on different environments without owning them.  [`[Refer this]`](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)

### How it works ? 
- Triggers 🔫 on `issue_comment` whenever a new issue comment is been made.
- Gets pip cache and install 🔻 dependencies. 
- Runs the input in the comment message. 
- Comments you back with code execution. 

### How to make this yours ?
- Star ⭐and Fork 🍴 [this repo.](https://github.com/jainamoswal/GitHub-IDE/fork)
- Add or delete your requirements for pip modules from 👷 [requirements.txt](./requirements.txt).
- Go to your repo's ⚠️ issue section. 
- Make a new issue. _(It will not run one issue comment made while making an issue.)_
- **Assign yourself** and your teammates as to make sure only these users have access to the Action.
- Then comment 📝any code, Bot 🤖 will reply you back in 10 seconds.

### Note :~
- Show little support by staring this repo. ⭐
- Be careful, This is REPO is harmful as it contains GitHub PAT. So it can also delete or do anything from you GitHub account in Your GitHub account. **So do not assign anyone in issues whom you don't trust.**
- Use this REPO at your own risk, I'm not resposible for any of your losses.
- For any security suggestions, Contact me on [social media.](https://github.com/jainamoswal)

<details>
  <summary><b>:v: &nbsp;Support me</b></summary>
  <br/>
  <p align="center">
    <a href="https://paypal.com/paypalme/JOswal105">
        <img height="40px" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" />
    </a> &nbsp;
    <a href="https://buymeacoffee.com/jainamoswal">
        <img height="40px" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" />
    </a> &nbsp;
    <a href="https://ko-fi.com/O5O64S9GG">
        <img height="40px" src="https://cdn.ko-fi.com/cdn/kofi3.png?v=2" />
    </a> &nbsp;
    <a href="https://upier.org/pay?vpa=jainamoswal@sbi&amount=250">
        <img height="40px" src="https://upload.wikimedia.org/wikipedia/commons/archive/e/e1/20200901100646%21UPI-Logo-vector.svg" />
    </a>
  </p>
  
</details>

---

## License 
### [GitHub-IDE](https://github.com/jainamoswal/GitHub-IDE) is licensed under [GNU Affero General Public License v3](https://www.gnu.org/) or later.

[![License](https://www.gnu.org/graphics/gplv3-or-later.png)](LICENSE)

`The GNU General Public License (GNU GPL or simply GPL) is a series of widely-used free software licenses that guarantee end users the freedom to run, study, share, and modify the software.[8] The licenses were originally written by Richard Stallman, founder of the Free Software Foundation (FSF), for the GNU Project, and grant the recipients of a computer program the rights of the Free Software Definition.[9] The GPL series are all copyleft licenses, which means that any derivative work must be distributed under the same or equivalent license terms. This is in distinction to permissive software licenses, of which the BSD licenses and the MIT License are widely used, less restrictive examples. GPL was the first copyleft license for general use.`
