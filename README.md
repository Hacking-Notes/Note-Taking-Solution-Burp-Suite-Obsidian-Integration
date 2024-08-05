
# Collaborative Note-Taking Guide & Tools for Bug Bounty Hunting (BETA)

![New Project (2)](https://github.com/user-attachments/assets/50310567-9135-4f51-9d9a-6258e88e0b3d)

Have you ever wondered what the best methodology for taking notes is, or do you put all the information on a single page and spend ages trying to find the details later? I have a solution for you! I will share a set of standards and methodologies I've used in the past that have helped me generate multiple bounties. I'll also reveal the tool I've created, the structure I use for taking notes, and my process for collaborating on note-taking.

## Setup & Requirements:

**General Steps**
- Install [Obsidian](https://obsidian.md/)
- Download the Obsidian folder (which includes pre-installed plugins) and place it into your Proton Drive using File Explorer.
- Add the [Obsidian Burp Suite extension](https://github.com/Hacking-Notes/collaborative-note-taking-guide-bug-bounty-tools/blob/main/Obsidan_BurpSuite.py) to your Burp extension

**Additional Steps for Collaboration**
- Create a [Proton account](https://proton.me/support/set-up-proton-drive)
- Install [Proton Drive](https://proton.me/drive/download)
- Install & setup [PeerDraft](https://www.peerdraft.app/) plugin in obsidian
- Purchase a subscription for the [Obsidian plugin](https://www.peerdraft.app/) ---> (~20$/YEAR)

## Methodology

The methodology for using the Burp Suite extension involves importing the target's structure into your Obsidian file. The extension automatically adds all domains within the scope to Obsidian and updates them as necessary. In Obsidian, document all relevant information for each website path and link these findings to the main file, where you briefly describe each issue or noteworthy detail. This approach helps maintain organized notes and avoids the inefficiency of consolidating all information into a single file, making it easier to retrieve specific details later.

<br>

<table>
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

<table>
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

To use Obsidian collaboratively, you need to determine two key aspects. First, decide if your collaborator needs to create new files or contribute to the website mapping. If the collaborator does not need or want to contribute to this aspect, simply share the Peer Draft link (refer to [Peer Draft documentation](https://github.com/peerdraft/obsidian-plugin) for details).

If you want your collaborator to contribute, you must provide them access to your Proton Drive account. This allows them to push the URLs they find in Burp directly to Proton-drive updating while you file structure on our end. Collaborators can only add a file by manually placing it in the Proton Drive folder. Moving a document within Obsidian and dragging it to the shared folder (for the invited collaborator) will not work. Therefore, the invited collaborator must manually open File Explorer and drag the new file into the Proton Drive folder.

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
        <li>Use the PeerDraft link inside Obsidian (PeerDraft plugin is required).</li>
        <li>Upload your Burp results (web topology) to the Proton Drive.</li>
        <li>Wait a few minutes and continue working on the newly added files.</li>
      </ul>
    </td>
  </tr>
</table>

<br>

This approach allows both collaborators to contribute to the website's topology. Each collaborator can add their findings, potentially discovering elements the other may have missed, thereby expanding the target's scope.

---

If you have any questions, suggestions, or issues regarding the roadmap or this repository, feel free to open an issue or reach out to me via Discord.

  <a href="https://discord.com">
  <img width="300" src="https://github.com/Hacking-Notes/Hacking-Notes/assets/118412415/5f34c47e-8f9e-40ef-885d-91ee9a6c5989" alt="gif">
  </a>



