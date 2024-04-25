
# kodey-langchain-sample

This repository is an example Kodey.ai Coding Agent Workflow

## Objectives

In this sample, we will explore how Kodey.ai can create projects and tools with langhcain and automate it.

## Project Setup & Steps 

1. Signup for a new Kodey.ai account or login to your existing Kodey.ai environmenty (link-here)
2. Configure your Kodey.ai integrations to the desired issue tracker and cloud git provider.
3. Fork this repository, and clone it to the cloud git provider of your choosing (Github, Azure DevOps, Bitbucket)
4. Create a new branch dev in your repo. Kodey will create new branches out of dev branch.
5. Create the sample issue / work item in your issue tracker. Copy and Paste the issue description from below.
6. Execute the below prompt in the Kodey.ai chat UI
7. Validate the commits and pull requests in your cloud git provider

### SAMPLE PROMPT - Github Tools (Creating a custom twillio tool with langchain)
```
    platform: github

    repository to work on: kodey-langchain-custom-tool

    branch name to create: feature/langchain-custom-tool-integration-v2

    Information to agent: Do as the steps below are defined one by one. You are working in github repo so make sure to use tools related to github repo. NOTE: You should write the actual implementation of code not just comments. Credentials required should be read from environment variable not from user's input.

    Steps:

    step 1: Create a new branch with name first and then do the steps below.

    step 2: Using WebCrawler Tool , Understand how to send message using python with twillio from url https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages/python

    step 3: Using tool_creator_template tool, get the template to create a new tool and understand how to create a new tool using langchain, how to pass the inputs to the tool, how to provide example for the input to tool.

    step 4: Create a new python file inside tools directory called twilio.py and make the tool to send message using twilio api using above understanding of twilio library and tool creation. NOTE: The description of the tool should be clear and should explain what inputs are required. It should provide example of input as given by the tool creation template. Input to the tool should be similar to the example provided. Also provide an example of the input in the tool description.

    step 5: Using WebCrawler Tool, understand how to use langchain openai chat llm from url https://python.langchain.com/docs/integrations/chat/openai/ and also understand how to initialize agent from langchain documentation url https://api.python.langchain.com/en/latest/agents/langchain.agents.initialize.initialize_agent.html and also

    step 5: Using above undetstanding Create a main file in root directory that initializes the langchain agent and uses above created twilio tool. Use open ai model "gpt-4-0125-preview" when initializing llm. The main file should accept input in plain natural language as system argument from user and pass it to agent while invoking.

    step 6: Create a new file requirements.txt in root directory and add all the dependencies required to run the project.

    step 7: Create a new pull request from the above created branch with title "Twilio Custom Tool API Tool Added v2".

    step 8: Update this issue status to closed.

```

### SAMPLE PROMPT - Azure DevOps Tools (Creating a custom twillio tool with langchain)
```
    platform: Azure

    repository to work on: kodey-langchain-custom-tool

    branch name to create: feature/langchain-custom-tool-integration-v2

    Information to agent: Do as the steps below are defined one by one. You are working in azure repo so make sure to use tools related to azure repo. NOTE: You should write the actual implementation of code not just comments. Credentials required should be read from environment variable not from user's input.

    Steps:

    step 1: Create a new branch with name first and then do the steps below.

    step 2: Using WebCrawler Tool , Understand how to send message using python with twillio from url https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages/python

    step 3: Using tool_creator_template tool, get the template to create a new tool and understand how to create a new tool using langchain, how to pass the inputs to the tool, how to provide example for the input to tool.

    step 4: Create a new python file inside tools directory called twilio.py and make the tool to send message using twilio api using above understanding of twilio library and tool creation. NOTE: The description of the tool should be clear and should explain what inputs are required. It should provide example of input as given by the tool creation template. Input to the tool should be similar to the example provided. Also provide an example of the input in the tool description.

    step 5: Using WebCrawler Tool, understand how to use langchain openai chat llm from url https://python.langchain.com/docs/integrations/chat/openai/ and also understand how to initialize agent from langchain documentation url https://api.python.langchain.com/en/latest/agents/langchain.agents.initialize.initialize_agent.html and also

    step 5: Using above undetstanding Create a main file in root directory that initializes the langchain agent and uses above created twilio tool. Use open ai model "gpt-4-0125-preview" when initializing llm. The main file should accept input in plain natural language as system argument from user and pass it to agent while invoking.

    step 6: Create a new file requirements.txt in root directory and add all the dependencies required to run the project.

    step 7: Create a new pull request from the above created branch with title "Twilio Custom Tool API Tool Added v2".

    step 8: Update this issue status to DONE.
```

### SAMPLE PROMPT - Jira / Bitbucket (Creating a custom twillio tool with langchain)
```

    platform: Bitbucket

    repository to work on: kodey-langchain-custom-tool

    branch name to create: feature/langchain-custom-tool-integration-v2

    Information to agent: Do as the steps below are defined one by one. You are working in bitbucket repo so make sure to use tools related to bitbucket repo. NOTE: You should write the actual implementation of code not just comments. Credentials required should be read from environment variable not from user's input.

    Steps:

    step 1: Create a new branch with name first and then do the steps below.

    step 2: Using WebCrawler Tool , Understand how to send message using python with twillio from url https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages/python

    step 3: Using tool_creator_template tool, get the template to create a new tool and understand how to create a new tool using langchain, how to pass the inputs to the tool, how to provide example for the input to tool.

    step 4: Create a new python file inside tools directory called twilio.py and make the tool to send message using twilio api using above understanding of twilio library and tool creation. NOTE: The description of the tool should be clear and should explain what inputs are required. It should provide example of input as given by the tool creation template. Input to the tool should be similar to the example provided. Also provide an example of the input in the tool description.

    step 5: Using WebCrawler Tool, understand how to use langchain openai chat llm from url https://python.langchain.com/docs/integrations/chat/openai/ and also understand how to initialize agent from langchain documentation url https://api.python.langchain.com/en/latest/agents/langchain.agents.initialize.initialize_agent.html and also

    step 5: Using above undetstanding Create a main file in root directory that initializes the langchain agent and uses above created twilio tool. Use open ai model "gpt-4-0125-preview" when initializing llm. The main file should accept input in plain natural language as system argument from user and pass it to agent while invoking.

    step 6: Create a new file requirements.txt in root directory and add all the dependencies required to run the project.

    step 7: Create a new pull request from the above created branch with title "Twilio Custom Tool API Tool Added 

    step 8: Update this issue status to DONE in jira.

```

## Once you have set the description of the issue in your relavant system. You need to use kodey UI Chat and execute below statement to get the work done. 

### Github Issue and Github Repo
```
   Get the issue with id <issue_id> from github repo and do as the description of the issue says.
```

### Azure Repo Issue and Azure Repo
```
   Get the issue with id <issue_id> from azure repo and do as the description of the issue says.
```

### Jira Issue and Bitbucket Repo
```
   Get the issue with id <issue_id> from jira and do as the description of the issue says.
```

## Confirming Successful Sample Outputs

1. Confirm that the branch was created on the issue / work item
2. Confirm that the code created in the associated pull request contains the following
3. Confirm that the work item/issue/ticket in your relevant issue tracking platform is updated.%