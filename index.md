# Computer Science Capstone
  
## <center>CS-499 | SNHU</center>

#### CODE REVIEW

Code reviews are critical for maintaining code quality, fostering collaboration, and reducing technical debt. They allow developers to identify bugs, inefficiencies, or deviations from best practices early, preventing costly fixes later. Code reviews also promote knowledge sharing among team members, improving collective expertise and ensuring consistent adherence to coding standards. Additionally, they provide a platform for mentoring and constructive feedback, fostering a culture of continuous learning and accountability. Ultimately, this process enhances the overall reliability, maintainability, and security of the codebase, contributing to the long-term success of software projects. 

<code>You can watch the code review <a href="https://www.youtube.com/watch?v=N_TAyv-Cbd4">here</a>.</code>

## Professional Self-Assessment

Completing the coursework throughout the Computer Science program and developing the ePortfolio has been a great experience which allowed me to showcase my technical strengths, professional goals and values, and prepare for a career in the computer science field. There was an array of diverse projects and assignments that provided me the opportunity to demonstrate key skills. I was able to adaptably work with multiple programming languages while making enhancements to entirely different languages. This required technical expertise and the ability to learn and implement new tools and libraries quickly. Through my ePortfolio, I highlighted my proficiency in leveraging libraries and packages, integrating them seamlessly into programs, and creating functional, user-oriented solutions. My work on algorithms and data structures further showcased my analytical abilities. For instance, implementing insertion sort in one of my enhancements demonstrated how I can break down complex concepts into manageable components. This experience solidified my understanding of algorithmic principles and their practical applications, critical skills for solving real-world problems efficiently. A significant strength I developed is in database design and integration. By enhancing existing programs with database functionality, I demonstrated my ability to refactor code for modularity and usability. These projects taught me to think beyond conventional tools, finding creative solutions when resources were limited. For example, I successfully integrated a database without relying on tools proving my ability to innovate under constraints.
Beyond technical skills, the program shaped my professional goals and values, particularly in collaboration and communication. Working with peers on shared servers emphasized the importance of teamwork in achieving collective success. Whether offering help or seeking guidance, these interactions mirrored the collaborative dynamics of a professional environment. Additionally, navigating vague requirements taught me the value of proactive communication with stakeholders to ensure clarity and alignment an essential skill for delivering quality software. The program’s emphasis on software security also influenced my approach to development. Adhering to best practices, such as input validation and resource management, became second nature, preparing me to create secure and reliable systems. These experiences reinforced the importance of accountability and attention to detail in professional settings. Overall, the coursework and ePortfolio have been pivotal in preparing me for the computer science field. They have not only strengthened my technical abilities but also instilled values like collaboration, creativity, and continuous learning, making me more employable and confident as I embark on my career.

My portfolio showcases my technical growth and expertise through enhancements made to a text-based game, Battle at Mystery Manor Text Adventure Game. This adventure-based game requires players to navigate interconnected rooms, collect items, and strategize to defeat a boss. I enhanced the game to demonstrate key computer science skills, including algorithms, data structures, software design, and database integration. Notable improvements include implementing a breadth-first search (BFS) with a deque for shortest-path navigation, a priority queue for managing time-sensitive events, and modular classes like Room and RoomGraph to ensure scalability and reusability. These additions highlight my ability to design efficient and modular systems while leveraging built-in data structures for robust functionality.To expand the game’s features, I introduced commands for inventory management, room descriptions, and high-score tracking. Using the json module, I implemented a simple database to manage high scores with functions for saving, loading, and displaying the leaderboard. Additional enhancements, such as dynamic boss encounters enabled by the random module, added complexity and engagement. The modular design reduces interdependencies, simplifies vulnerability detection, and ensures the artifact is adaptable for future development. Together, these improvements demonstrate my proficiency in software engineering, algorithmic thinking, and database integration, reflecting the breadth of my computer science skills.


#### Project 1: Software Engineering and Design

I chose to use a text-based game titled “Battle at Mystery Manor Text Adventure Game”. The text-based game is an adventure-based game that contains different rooms that each contain an item. Players will need to collect every single item prior to reaching the final room to defeat the boss and win the game. The artifact was enhanced by adding several new features. First, I included brief descriptions for each room in the game to provide more context. Next, I implemented a limited inventory management system, increasing the game's difficulty by requiring players to strategize which items to keep. Additionally, I introduced new commands such as *examine* to view room descriptions, *drop* to remove an item from the inventory, and *inventory* to display all currently held items. Finally, I integrated the random module, enabling the possibility of encountering the boss before collecting all required items, which leads to losing the game.
<center>
  <a href="https://github.com/victorzs78/ePortfolio">
  </a>
</center>
  
<code>See the artifact's report and code <a href="https://github.com/victorzs78/ePortfolio/tree/main/Enhancement%20One%3A%20Software%20Design%20and%20Engineering">here</a>.</code>

#### Project 2: Algorithms and Data Structures

The text-based game was used again for this category. The artifact was enhanced to showcase algorithms, data structures, and software design principles. Dictionaries like "RoomGraph" store rooms and connections, while "Room" objects manage individual room details. A queue implemented with `deque` supports breadth-first search (BFS) for finding the shortest path in the game's map, demonstrating graph traversal and algorithmic thinking. A priority queue manages time-sensitive game events, adding complexity and real-time functionality. 

Classes like `Room` and `RoomGraph` ensure modularity, scalability, and reusability, with methods such as `add_neighbor` and `show_item_history` providing a clear API. Additional commands were added for inventory checks, room item history, and shortest path navigation to goals like the "Library." Room connections were designed to be bidirectional for realism, and built-in structures like `deque` and `heapq` reduced unnecessary complexity. These improvements highlight proficiency in essential software development skills. 

<center>
  <a href="https://github.com/victorzs78/victorzs78.github.io/new/main" title="Click me to view the artifact report">
  </a>
</center>
  
<code>See the artifact's report and code <a href="https://github.com/victorzs78/ePortfolio/tree/5e4915780a6533eabcc211571e217a7896063829/Enhancement%20Two%3A%20Algorithms%20and%20Data%20Structure">here</a>.</code>

#### Project 3: Databases

The text-based game was used again for this category. The artifact was enhanced to demonstrate effective use of a database. The `json` module was used to read and write high scores to a JSON file serving as a simple database. High score management was implemented with three functions: `load_highscores()` reads high scores or returns an empty list if the file is absent, `save_highscore(player_name, score)` adds a score, sorts the list, and saves the top 10, and `display_highscores()` prints the leaderboard when users input "highscores." Scores are saved when players win, prompting them to enter their name and moves made.

The modular design of classes like `Room` and `RoomGraph` reduces interdependencies, making vulnerabilities easier to detect and address. The `Room` class uses a deque to track item history, providing an audit trail to identify unintended or malicious behavior.
<center>
  <a href="https://github.com/victorzs78/victorzs78.github.io/new/main">
  </a>
</center>

  <code>See the artifact's report and code <b><a href="https://github.com/victorzs78/ePortfolio/tree/main/Enhancement%20Three%3A%20Databases" title="Click me to view the artifact report">here</a></b>.</code>

