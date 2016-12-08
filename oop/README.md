# The story
It's 2020. The mentors of Codecool Phnom Pen (capital of Cambodia) are fed up, that despite the strict house rules, no one cares about collecting the waste in a selective way in the school. They decided to make an automated dustbin, which can detect different types of garbage, and can put them to different containers automatically.

Mentors at Codecool usually have a whole bunch of things to do, and they aren't exceptions either, so they don't have time to implement the dustbin's software. Luckily it's internal computer is capable of running Python scripts...

Have you found out yet??? YES, it's your job to implement it in an Object-Oriented way! :-)

# The specification
Please find the following files in this directory:

### ```garbage.py```
This is the file containing a regular garbage's business logic.

##### Attributes
* name: a string, stroring some custom name of the exact garbage object

### ```paper_garbage.py```
This is the file containing the business logic of a garbage made of paper. PaperGarbage class inherits the logic of the Garbage class.

##### Attributes
* name: a string, stroring the name of the garbage (should be inherited from the Garbage)
* is_squeezed: a Boolean, storing if the garbage is squeezed (True) or not (False)

##### Instance methods
###### ```squeeze()```
* when called, it sets the object's is_squeezed attribute to True

### ```plastic_garbage.py```
This is the file containing the business logic of a garbage made of plastic. PlasticGarbage class inherits the logic of the Garbage class.

##### Attributes
* name: a string, stroring the name of the garbage (should be inherited from the Garbage)
* is_clean: a Boolean, storing if the garbage is clean (True) or not (False)

##### Instance methods
###### ```clean()```
* when called, it sets the object's is_clean attribute to True

### ```dustbin_content_error.py```
This file contains a custom exception, called DustbinContentError, which is raised by the Dustbin in some error cases (see below). It's already implemented, so you don't have to touch this file at all.

### ```dustbin.py```
This file should contain all the logic, what our automated dustbin can do.

##### Attributes
* color: a string, storing the dustbin's color
* paper_content: a list, storing PaperGarbage instances
* plastic_content: a list, storing PlasticGarbage instances
* house_waste_content: a list, storing Garbage instances

##### Intance methods
###### ```throw_out_garbage(garbage)```
* Receives an argument.
* If the argument is an instance of the PlasticGarbage class, and it's clean, then it puts that into the plastic_content list. If the PlasticGarbage instance is not clean, it raises a DustbinContentError exception.
* If the argument is an intance of the PaperGarbage class, and it's squeezed, then it puts that into the paper_content list. If the PaperGarbage instance is not squeezed, it raises a DustbinContentError exception.
* if the argument is an instance of the Garbage class (but not a PaperGarbage or a PlasticGarbage), then it puts that into the house_waste_content list
* if the argument is not an instance of the classes above, it raises a DustbinContentError exception.

###### ```empty_contents()```
* If it's called, plastic_content, paper_content and house_waste_content lists get emptied

### ```test.py```
This file contains test cases for the specification above. You mustn't touch it, but it worth checking it, as it can help understand the specification above.
You're ready with your assignment when all the tests run with success. You can run them with the usual command ```python test.py```
