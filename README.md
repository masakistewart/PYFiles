# PYFiles
A Python folder and file system creator. Edit the code to your heart's content!

- Creates nested folders in a predifined order
- Implementing an auto create system for different frameworks
	
	Use -a for an Angular boilerplate



#####Example:
		
		python3 pyfi.py /this/file/path/and/file.txt
		
#####Output:


		this
		└── file
    		└── path
        		└── and
            		└── file.txt
		
####If you want to chain multiple folders and files on a same level simply:

*every branch in a folder must be added this/that+other this/that/thing this/other/text.txt


#####Example
	python3 pyfi.py folder1+folder2 /folder2/folder3 


#####Output


		    .
			├── folder1
			└── folder2
    			└── folder3
				
####You may currently use Auto Create* for angular like so:
*more frameworks will be added in the future


#####Example:

		python3 pyfi.py -a
		
#####Output

		app
		├── public
		│   ├── css
		│   ├── fonts
		│   ├── img
		│   ├── js
		│   │   ├── app.js
		│   │   ├── controllers
		│   │   └── directives
		│   ├── model
		│   └── views
		│       ├── index.html
		│       └── templates
		└── server.js


 
				
