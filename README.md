## Customer service Improvement

this challenge is how to improve customer services. When the customer request is recieved, corresponding task and subtasks will be created and assigned to employees 
with plan date (when the task is supposed to be ended) and actual date (when task is ended in real). Some tasks will be delayed and actual date value becomes greater than plan date.  
Our solution is to find the root causes of delayed tasks by **statistical approach such as Kruskal Wallis**. Then within each recognized feature, we dive into its categories to know from which the differences are coming by using **post_hoc tests like Dunn**. The results cannot be demonstrated because of confidential issues.  
Python Libraries : **mstats, scikit_posthocs**

