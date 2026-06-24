# VIRTUAL ENVIRONMENT:
# As we start working on more python projects, we are likely to use different versions of libraries.
# Virtual Environments help us isolate project dependencies, preventing conflicts between different projects.


# Here are different versions of our project using different versions of dependencies, suppose after few months the package gets upgraded then virtual env 
# help us install different versions of libraries for our particular project.

# version_1 -----uses---- package_1 (pandas_1.0.5)
# version_2 -----uses---- package_2 (numpy_2.0.9)
# version_3 -----uses---- package_3 (moviepy_3.0.5)

 

# Also a virtual environment is a self- contained directory that contains its own Python interpreter and libraries. 
# This means that libraries installed in one virtual environment will not with libraries in another environment.


#---------------------------------------------------#---------------------------------------------------#---------------------------------------------------#
# Creating a virtual environment (using venv - recommended):

'''python -m venv my_env'''  # Creates a virtual environment named "my_env" ==> Python my message is that create a virtual env. named 'my_env'

# Activating the virtual environment:
'''my_env/Scripts/activate'''

#---------------------------------------------------#---------------------------------------------------#---------------------------------------------------#

# NOTE: Sometimes windows cmd shows error like "running scripts is disabled on this system" so at this time we perform tweaks with the execution poplicy scope:
'''Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process'''
# Then again running the '''my_env/Scripts/activate''' coomand in cmd ----> this will activate the virtual environment.


# Once activated, we’ll see the virtual environment’s name in our terminal/command prompt (e.g., (my_env)).

#---------------------------------------------------#---------------------------------------------------#---------------------------------------------------#
# To deactivate the virtual environment we simply type:
"""deactivate"""