
# Collaborative Note-Taking Guide & Tools for Bug Bounty Hunting

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
- Purchase a subscription for the [Obsidian plugin](https://www.peerdraft.app/) ---> (~20$/YEAR) **NOT REQUIRED IF COLLABORATION IS NOT YOUR INTEREST**

## Methodology

The methodology for using the Burp Suite extension involves importing the target's structure into your Obsidian file. The extension automatically adds all domains within the scope to Obsidian and updates them as necessary. In Obsidian, document all relevant information for each website path and link these findings to the main file, where you briefly describe each issue or noteworthy detail. This approach helps maintain organized notes and avoids the inefficiency of consolidating all information into a single file, making it easier to retrieve specific details later.

| Root Domain (Target) | Domain / Subdomains | Paths | Endpoints|
| -------------------- | ------------------- | ----- | -------- |


**Import your target's structure into Obsidian:**

1. **Update your web topology**: Go to the Obsidian extension in BurpSuite, select your Obsidian Folder (Bug Bounty Shared) within Proton Drive, and click "Generate" with the appropriate protocol type. This action will create the website topology in Obsidian.
2. **Organize your notes**: At the root level of the domain, create two files:
   - **Daily Notes**: Use this file to track what has been done and to avoid duplicating efforts. It also informs collaborators about completed tasks.
   - **Main Notes**: This file should contain all significant observations or vulnerabilities found. Link these notes to the relevant pages and include only a brief description of the vulnerabilities or noteworthy elements discovered.

PS: Note that once you discover additional paths in Burp, simply click "Generate" in the Burp extension to add the newly discovered paths.

## Collaboration

For using collaratively Obsidian, you need to determine two things. First does your collaborator need to create new files/contribute to the website mapping, or not. If the collaborator does not need/want to contribute to this aspect, then just share the peer draft link (Peerdraf documentation). If you want your collaborator to contribute, then you will need to provide the other collaborator with your proton drive account so he can push the URLs he found on his end and create files. At the moment, the only way a contributor can add a file is by manually dropping a file in the Proton-drive folder. Moving a document inside Obsidian and dragging it (for the collaborator who got invited) to the shared folder will not work. So the invited collaborator will need to manually open File Explorer and drag the new file inside the Proton drive folder

### Collaborator adding file


