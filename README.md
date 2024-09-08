
# A Streamlined Note-Taking Solution - Burp Suite Obsidian Integration 

![354929916-50310567-9135-4f51-9d9a-6258e88e0b3d (4)](https://github.com/user-attachments/assets/530dca62-d775-49cd-82ca-8c2cdb18038e)

Are you struggling to organize your security research notes effectively? Do you often dump all your information on a single page, only to waste time later searching for crucial details? I’ve got the perfect solution for you!

I've developed a powerful Burp Suite extension that integrates seamlessly with Obsidian, offering a structured and efficient way to take notes, track vulnerabilities, and manage your bug bounty process. This tool and methodology have been instrumental in helping me secure multiple bounties, and now I'm sharing it with you.

Key Features:
- Standardized Note-Taking Methodology: A clear structure to help you organize findings, categorize vulnerabilities, and link key information for quick access.
- Collaboration-Ready: Use third-party cloud providers to easily share notes and collaborate on security research.
- Folder and File Organization: Automatically convert Burp Suite output into an organized folder structure, making it easier to navigate through projects.

With this tool, you'll spend less time searching for details and more time discovering vulnerabilities.

## Setup & Requirements (Obsidian BurpSuite Extension):

**General Steps**
- Install [Obsidian](https://obsidian.md/)
- Download the Obsidian folder (which includes pre-installed plugins).
- Add the [Obsidian Burp Suite extension](https://github.com/Hacking-Notes/collaborative-note-taking-guide-bug-bounty-tools/blob/main/Obsidan_BurpSuite.py) to your Burp extension

![burp_obsidian](https://github.com/user-attachments/assets/923d093d-e41a-486b-8bfe-39bc335d0296)

**Additional Steps for Collaboration**
- Create a [Proton account](https://proton.me/support/set-up-proton-drive) (Or any other third-party cloud provider that offers storage services)
- Install [Proton Drive](https://proton.me/drive/download)
- Purchase a Obsidian Sync Subscription [Obsidian Sync]([https://www.peerdraft.app/](https://obsidian.md/sync)) ---> (~50$/YEAR)

## Methodology

The methodology for using the Burp Suite extension involves importing the target's structure into your Obsidian file. The extension automatically adds all domains within the scope to Obsidian and updates them as necessary. In Obsidian, document all relevant information for each website path and link these findings to the main file, where you briefly describe each issue or noteworthy detail. This approach helps maintain organized notes and avoids the inefficiency of consolidating all information into a single file, making it easier to retrieve specific details later.

<br>

<table border="1">
  <tr>
    <th>Root Domain (Target)</th>
    <th>Domain / Subdomains</th>
    <th>Paths</th>
    <th>Endpoints</th>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/549f66af-9491-4e91-8d8c-7b96e560cb19" alt="Root Domain (Target)"></td>
    <td><img src="https://github.com/user-attachments/assets/e7cba72e-0fa7-44be-8b7e-841925ef88b9" alt="Domain / Subdomains"></td>
    <td><img src="https://github.com/user-attachments/assets/a08ab669-37da-4564-bd22-9298636af2c6" alt="Paths"></td>
    <td><img src="https://github.com/user-attachments/assets/145873f3-e4e1-435e-97db-aff1cc811c53" alt="Endpoints"></td>
  </tr>
</table>

<br>

**Import your target's structure into Obsidian:**

1. **Update your web topology**: Go to the Obsidian extension in BurpSuite, select your Obsidian Folder (Bug Bounty Shared) within Proton Drive, and click "Generate" with the appropriate protocol type. This action will create the website topology in Obsidian. [View Example](https://github.com/user-attachments/assets/1e97c6c2-f034-4b17-9218-1fbfcc63f048)
2. **Organize your notes**: At the root level of the domain, create two files:
   - **Daily Notes**: Use this file to track what has been done and to avoid duplicating efforts. It also informs collaborators about completed tasks.
   - **Main Notes**: This file should contain all significant observations or vulnerabilities found. Link these notes to the relevant pages and include only a brief description of the vulnerabilities or noteworthy elements discovered.

<br>

<table border="1">
  <tr>
    <th>Main Notes</th>
    <th>Daily Notes</th>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/4bcc2544-18f8-4cfb-887d-7d711e72b12e" alt="Root Domain (Target)"></td>
    <td><img src="https://github.com/user-attachments/assets/18883a02-4a47-4976-a638-799713e0fcca" alt="Domain / Subdomains"></td>
  </tr>
</table>

<br>

This methodology enables efficient categorization, ensuring that all your notes and files are systematically organized. By using this approach, you can quickly and easily review your files and notes with just a single click, eliminating the need to search for hours. This structured method saves time and enhances your productivity by providing quick access to all relevant information whenever needed. Whether you are tracking vulnerabilities, documenting findings, or collaborating with others, this streamlined process ensures that everything is at your fingertips, making your work more efficient and effective.

**PS: Once you discover additional paths in Burp, click "Generate" in the Burp extension to add the newly discovered paths.**

## Collaboration

To use Obsidian collaboratively, you need to determine two key aspects. First, decide if your collaborator needs to create new files or contribute to the website mapping. If the collaborator does not need or want to contribute to this aspect, simply share the project with Obsidian Sync (refer to [Obsidian documentation](https://help.obsidian.md/Obsidian+Sync/Introduction+to+Obsidian+Sync) for details).

The concept is straightforward: upload the Obsidian folder to a third-party cloud provider (e.g., Proton Drive, which offers a free plan) that is accessible via a file explorer, and share the account with your collaborator. This setup allows both you and your collaborator to contribute directly to the same Obsidian vault. It's especially useful if your collaborator discovers subdomains or paths that you haven't found, as they can add them directly to the shared folder.

For seamless collaboration, you must purchase an [Obsidian Sync subscription ($50/year)](https://obsidian.md/sync). I've tried various third-party tools, but none offer the same level of encryption and affordability that Obsidian provides.
<br>

<table border="1">
  <tr>
    <th>File Owner</th>
    <th>Invited Collaborator</th>
  </tr>
  <tr>
    <td>
      <ul>
        <li>Share the Proton Drive account information.</li>
        <li>Share the PeerDraft link with the collaborator.</li>
        <li>Create files as needed.</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>Login to the Proton Drive account.</li>
        <li>Upload your Burp results (web topology) to the Proton Drive.</li>
        <li>Wait a few minutes and continue working on the newly added files.</li>
      </ul>
    </td>
  </tr>
</table>

To invite your collaborator, go to Obsidian's settings, select "Sync," and then choose "Manage." From there, you can send an invitation to allow them to join and collaborate in your shared vault.

<p align="left">
  <img src="https://github.com/user-attachments/assets/7f56aac1-4cc8-4869-ac00-8c54312ca301" alt="Description of image">
</p>

This method enables collaborators to contribute to the company topology, allowing each to share their findings.

---

If you have any questions, suggestions, or issues regarding the roadmap or this repository, feel free to open an issue or reach out to me via Discord.

  <a href="https://discord.com">
  <img width="300" src="https://github.com/Hacking-Notes/Hacking-Notes/assets/118412415/5f34c47e-8f9e-40ef-885d-91ee9a6c5989" alt="gif">
  </a>



