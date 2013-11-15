# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:40:49 2013

@author: Artur_Herczeg
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

import os
import urlparse


Base = declarative_base()

from domain import Capability

DATABASE_ENVVAR = "HEROKU_POSTGRESQL_RED_URL"


def createSessionClass(base=Base):
    if DATABASE_ENVVAR in os.environ:
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ[DATABASE_ENVVAR])

        engine = create_engine(URL(drivername="postgresql",
                                   username=url.username,
                                   password=url.password,
                                   host=url.hostname,
                                   port=url.port,
                                   database=url.path[1:]))
    else:
        engine = create_engine(
            'postgresql://postgres:pass123@localhost:5432/ProgCapMat',
            echo=True)

    base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session


def initDB(Session):
    initdata = [(1, "Computer Science", "Data structures", 0, "Doesn’t know the difference between Array and LinkedList"),
                (2, "Computer Science", "Data structures", 1, "Able to explain and use Arrays, LinkedLists, Dictionaries etc in practical programming tasks"),
                (3, "Computer Science", "Data structures", 2, "Knows space and time tradeoffs of the basic data structures, Arrays vs LinkedLists, Able to explain how hashtables can be implemented and can handle collisions, Priority queues and ways to implement them etc."),
                (4, "Computer Science", "Data structures", 3, "Knowledge of advanced data structures like B-trees, binomial and fibonacci heaps, AVL/Red Black trees, Splay Trees, Skip Lists, tries etc."),

                (5, "Computer Science", "Algorithms", 0, "Unable to find the average of numbers in an array (It’s hard to believe but I’ve interviewed such candidates)"),
                (6, "Computer Science", "Algorithms", 1, "Basic sorting, searching and data structure traversal and retrieval algorithms"),
                (7, "Computer Science", "Algorithms", 2, "Tree, Graph, simple greedy and divide and conquer algorithms, is able to understand the relevance of the levels of this matrix."),
                (8, "Computer Science", "Algorithms", 3, "Able to recognize and code dynamic programming solutions, good knowledge of graph algorithms, good knowledge of numerical computation algorithms, able to identify NP problems etc."),

                (9, "Computer Science", "Systems programming", 0, "Doesn't know what a compiler, linker or interpreter is"),
                (10, "Computer Science", "Systems programming", 1, "Basic understanding of compilers, linker and interpreters. Understands what assembly code is and how things work at the hardware level. Some knowledge of virtual memory and paging."),
                (11, "Computer Science", "Systems programming", 2, "Understands kernel mode vs. user mode, multi-threading, synchronization primitives and how they’re implemented, able to read assembly code. Understands how networks work, understanding of network protocols and socket level programming."),
                (12, "Computer Science", "Systems programming", 3, "Understands the entire programming stack, hardware (CPU + Memory + Cache + Interrupts + microcode), binary code, assembly, static and dynamic linking, compilation, interpretation, JIT compilation, garbage collection, heap, stack, memory addressing…"),

                (13, "Software Engineering", "Source code version control", 0, "Folder backups by date"),
                (14, "Software Engineering", "Source code version control", 1, "VSS and beginning CVS/SVN user"),
                (15, "Software Engineering", "Source code version control", 2, "Proficient in using CVS and SVN features. Knows how to branch and merge, use patches setup repository properties etc."),
                (16, "Software Engineering", "Source code version control", 3, "Knowledge of distributed VCS systems. Has tried out Bzr/Mercurial/Darcs/Git"),

                (17, "Software Engineering", "Build automation", 0, "Only knows how to build from IDE"),
                (18, "Software Engineering", "Build automation", 1, "Knows how to build the system from the command line"),
                (19, "Software Engineering", "Build automation", 2, "Can setup a script to build the basic system"),
                (20, "Software Engineering", "Build automation", 3, "Can setup a script to build the system and also documentation, installers, generate release notes and tag the code in source control"),

                (21, "Software Engineering", "Automated testing", 0, "Thinks that all testing is the job of the tester"),
                (22, "Software Engineering", "Automated testing", 1, "Has written automated unit tests and comes up with good unit test cases for the code that is being written"),
                (23, "Software Engineering", "Automated testing", 2, "Has written code in TDD manner"),
                (24, "Software Engineering", "Automated testing", 3, "Understands and is able to setup automated functional, load/performance and UI tests"),

                (25, "Programming", "Problem decomposition", 0, "Only straight line code with copy paste for reuse"),
                (26, "Programming", "Problem decomposition", 1, "Able to break up problem into multiple functions"),
                (27, "Programming", "Problem decomposition", 2, "Able to come up with reusable functions/objects that solve the overall problem	"),
                (28, "Programming", "Problem decomposition", 3, "Use of appropriate data structures and algorithms and comes up with generic/object-oriented code that encapsulate aspects of the problem that are subject to change."),

                (29, "Programming", "Systems decomposition", 0, "Not able to think above the level of a single file/class"),
                (30, "Programming", "Systems decomposition", 1, "Able to break up problem space and design solution as long as it is within the same platform/technology"),
                (31, "Programming", "Systems decomposition", 2, "Able to design systems that span multiple technologies/platforms."),
                (32, "Programming", "Systems decomposition", 3, "Able to visualize and design complex systems with multiple product lines and integrations with external systems. Also should be able to design operations support systems like monitoring, reporting, fail overs etc."),

                (33, "Programming", "Communication", 0, "Cannot express thoughts/ideas to peers. Poor spelling and grammar."),
                (34, "Programming", "Communication", 1, "Peers can understand what is being said. Good spelling and grammar."),
                (35, "Programming", "Communication", 2, "Is able to effectively communicate with peers"),
                (36, "Programming", "Communication", 3, "Able to understand and communicate thoughts/design/ideas/specs in a unambiguous manner and adjusts communication as per the context"),

                (37, "Programming", "Code organization within a file", 0, "no evidence of organization within a file"),
                (38, "Programming", "Code organization within a file", 1, "Methods are grouped logically or by accessibility"),
                (39, "Programming", "Code organization within a file", 2, "Code is grouped into regions and well commented with references to other source files"),
                (40, "Programming", "Code organization within a file", 3, "File has license header, summary, well commented, consistent white space usage. The file should look beautiful."),

                (41, "Programming", "Code organization across files", 0, "No thought given to organizing code across files"),
                (42, "Programming", "Code organization across files", 1, "Related files are grouped into a folder"),
                (43, "Programming", "Code organization across files", 2, "Each physical file has a unique purpose, for e.g. one class definition, one feature implementation etc."),
                (44, "Programming", "Code organization across files", 3, "Code organization at a physical level closely matches design and looking at file names and folder distribution provides insights into design"),

                (45, "Programming", "Source tree organization", 0, "Everything in one folder"),
                (46, "Programming", "Source tree organization", 1, "Basic separation of code into logical folders."),
                (47, "Programming", "Source tree organization", 2, "No circular dependencies, binaries, libs, docs, builds, third-party code all organized into appropriate folders	"),
                (48, "Programming", "Source tree organization", 3, "Physical layout of source tree matches logical hierarchy and organization. The directory names and organization provide insights into the design of the system."),

                (49, "Programming", "Code readability", 0, "Mono-syllable names"),
                (50, "Programming", "Code readability", 1, "Good names for files, variables classes, methods etc."),
                (51, "Programming", "Code readability", 2, "No long functions, comments explaining unusual code, bug fixes, code assumptions"),
                (52, "Programming", "Code readability", 3, "Code assumptions are verified using asserts, code flows naturally – no deep nesting of conditionals or methods"),

                (53, "Programming", "Defensive coding", 0, "Doesn’t understand the concept"),
                (54, "Programming", "Defensive coding", 1, "Checks all arguments and asserts critical assumptions in code"),
                (55, "Programming", "Defensive coding", 2, "Makes sure to check return values and check for exceptions around code that can fail."),
                (56, "Programming", "Defensive coding", 3, "Has his own library to help with defensive coding, writes unit tests that simulate faults"),

                (57, "Programming", "Error handling	", 0, "Only codes the happy case"),
                (58, "Programming", "Error handling	", 1, "Basic error handling around code that can throw exceptions/generate errors"),
                (59, "Programming", "Error handling	", 2, "Ensures that error/exceptions leave program in good state, resources, connections and memory is all cleaned up properly"),
                (60, "Programming", "Error handling	", 3, "Codes to detect possible exception before, maintain consistent exception handling strategy in all layers of code, come up with guidelines on exception handling for entire system."),

                (61, "Programming", "IDE", 0, "Mostly uses IDE for text editing"),
                (62, "Programming", "IDE", 1, "Knows their way around the interface, able to effectively use the IDE using menus."),
                (63, "Programming", "IDE", 2, "Knows keyboard shortcuts for most used operations."),
                (64, "Programming", "IDE", 3, "Has written custom macros"),

                (65, "Programming", "API", 0, "Needs to look up the documentation frequently"),
                (66, "Programming", "API", 1, "Has the most frequently used APIs in memory"),
                (67, "Programming", "API", 2, "Vast and In-depth knowledge of the API"),
                (68, "Programming", "API", 3, "Has written libraries that sit on top of the API to simplify frequently used tasks and to fill in gaps in the API"),

                (69, "Programming", "Frameworks", 0, "Has not used any framework outside of the core platform"),
                (70, "Programming", "Frameworks", 1, "Has heard about but not used the popular frameworks available for the platform."),
                (71, "Programming", "Frameworks", 2, "Has used more than one framework in a professional capacity and is well-versed with the idioms of the frameworks."),
                (72, "Programming", "Frameworks", 3, "Author of framework"),

                (73, "Programming", "Requirements", 0, "Takes the given requirements and codes to spec"),
                (74, "Programming", "Requirements", 1, "Come up with questions regarding missed cases in the spec"),
                (75, "Programming", "Requirements", 2, "Understand complete picture and come up with entire areas that need to be speced"),
                (76, "Programming", "Requirements", 3, "Able to suggest better alternatives and flows to given requirements based on experience	"),

                (77, "Programming", "Scripting", 0, "No knowledge of scripting tools"),
                (78, "Programming", "Scripting", 1, "Batch files/shell scripts"),
                (79, "Programming", "Scripting", 2, "Perl/Python/Ruby/VBScript/Powershell"),
                (80, "Programming", "Scripting", 3, "Has written and published reusable code"),

                (81, "Programming", "Database", 0, "Thinks that Excel is a database"),
                (82, "Programming", "Database", 1, "Knows basic database concepts, normalization, ACID, transactions and can write simple selects"),
                (83, "Programming", "Database", 2, "Able to design good and normalized database schemas keeping in mind the queries that’ll have to be run, proficient in use of views, stored procedures, triggers and user defined types. Knows difference between clustered and non-clustered indexes. Proficient in use of ORM tools."),
                (84, "Programming", "Database", 3, "Can do basic database administration, performance optimization, index optimization, write advanced select queries, able to replace cursor usage with relational sql, understands how data is stored internally, understands how indexes are stored internally, understands how databases can be mirrored, replicated etc. Understands how the two phase commit works."),

                (85, "Experience", "Languages with professional experience", 0, "Imperative or Object Oriented	"),
                (86, "Experience", "Languages with professional experience", 1, "Imperative, Object-Oriented and declarative (SQL), added bonus if they understand static vs dynamic typing, weak vs strong typing and static inferred types	"),
                (87, "Experience", "Languages with professional experience", 2, "Functional, added bonus if they understand lazy evaluation, currying, continuations	"),
                (88, "Experience", "Languages with professional experience", 3, "Concurrent (Erlang, Oz) and Logic (Prolog)	"),

                (89, "Experience", "Platforms with professional experience", 0, "1"),
                (90, "Experience", "Platforms with professional experience", 1, "2-3"),
                (91, "Experience", "Platforms with professional experience", 2, "4-5"),
                (92, "Experience", "Platforms with professional experience", 3, "6+"),

                (93, "Experience", "Years of professional experience", 0, "1"),
                (94, "Experience", "Years of professional experience", 1, "2-5"),
                (95, "Experience", "Years of professional experience", 2, "6-9"),
                (96, "Experience", "Years of professional experience", 3, "10+"),

                (97, "Experience", "Domain knowledge", 0, "No knowledge of the domain"),
                (98, "Experience", "Domain knowledge", 1, "Has worked on at least one product in the domain."),
                (99, "Experience", "Domain knowledge", 2, "Has worked on multiple products in the same domain."),
                (100, "Experience", "Domain knowledge", 3, "Domain expert. Has designed and implemented several products/solutions in the domain. Well versed with standard terms, protocols used in the domain."),

                (101, "Knowledge", "Tool knowledge", 0, "Limited to primary IDE (VS.Net, Eclipse etc.)"),
                (102, "Knowledge", "Tool knowledge", 1, "Knows about some alternatives to popular and standard tools."),
                (103, "Knowledge", "Tool knowledge", 2, "Good knowledge of editors, debuggers, IDEs, open source alternatives etc. etc. For e.g. someone who knows most of the tools from Scott Hanselman’s power tools list. Has used ORM tools."),
                (104, "Knowledge", "Tool knowledge", 3, "Has actually written tools and scripts, added bonus if they’ve been published."),

                (105, "Knowledge", "Languages exposed to	", 0, "Imperative or Object Oriented"),
                (106, "Knowledge", "Languages exposed to	", 1, "Imperative, Object-Oriented and declarative (SQL), added bonus if they understand static vs dynamic typing, weak vs strong typing and static inferred types"),
                (107, "Knowledge", "Languages exposed to	", 2, "Functional, added bonus if they understand lazy evaluation, currying, continuations"),
                (108, "Knowledge", "Languages exposed to	", 3, "Concurrent (Erlang, Oz) and Logic (Prolog)"),

                (109, "Knowledge", "Codebase knowledge	", 0, "Has never looked at the codebase"),
                (110, "Knowledge", "Codebase knowledge	", 1, "Basic knowledge of the code layout and how to build the system"),
                (111, "Knowledge", "Codebase knowledge	", 2, "Good working knowledge of code base, has implemented several bug fixes and maybe some small features."),
                (112, "Knowledge", "Codebase knowledge	", 3, "Has implemented multiple big features in the codebase and can easily visualize the changes required for most features or bug fixes."),

                (113, "Knowledge", "Knowledge of upcoming technologies	", 0, "Has not heard of the upcoming technologies"),
                (114, "Knowledge", "Knowledge of upcoming technologies	", 1, "Has heard of upcoming technologies in the field"),
                (115, "Knowledge", "Knowledge of upcoming technologies	", 2, "Has downloaded the alpha preview/CTP/beta and read some articles/manuals"),
                (116, "Knowledge", "Knowledge of upcoming technologies	", 3, "Has played with the previews and has actually built something with it and as a bonus shared that with everyone else"),

                (117, "Knowledge", "Platform internals	", 0, "Zero knowledge of platform internals"),
                (118, "Knowledge", "Platform internals	", 1, "Has basic knowledge of how the platform works internally"),
                (119, "Knowledge", "Platform internals	", 2, "Deep knowledge of platform internals and can visualize how the platform takes the program and converts it into executable code."),
                (120, "Knowledge", "Platform internals	", 3, "Has written tools to enhance or provide information on platform internals. For e.g. disassemblers, decompilers, debuggers etc."),

                (121, "Knowledge", "Books	", 0, "Unleashed series, 21 days series, 24 hour series, dummies series…"),
                (122, "Knowledge", "Books	", 1, "Code Complete, Don’t Make me Think, Mastering Regular Expressions"),
                (123, "Knowledge", "Books	", 2, "Design Patterns, Peopleware, Programming Pearls, Algorithm Design Manual, Pragmatic Programmer, Mythical Man month"),
                (124, "Knowledge", "Books	", 3, "Structure and Interpretation of Computer Programs, Concepts Techniques, Models of Computer Programming, Art of Computer Programming, Database systems , by C. J Date, Thinking Forth, Little Schemer"),

                (125, "Knowledge", "Blogs	", 0, "Has heard of them but never got the time."),
                (126, "Knowledge", "Blogs	", 1, "Reads tech/programming/software engineering blogs and listens to podcasts regularly."),
                (127, "Knowledge", "Blogs	", 2, "Maintains a link blog with some collection of useful articles and tools that he/she has collected"),
                (128, "Knowledge", "Blogs	", 3, "Maintains a blog in which personal insights and thoughts on programming are shared"),]

    session = Session()
    for initdatarow in initdata:
        id, category, subcategory, level, desc = initdatarow
        capability = Capability(
            id=id,
            category=category,
            subcategory=subcategory,
            level=level,
            description=desc)

        res = session.query(Capability).filter(Capability.id == id).count()
        if res == 0:
            session.add(capability)

    session.commit()
