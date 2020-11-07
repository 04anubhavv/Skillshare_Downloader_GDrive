import sys, os
from skillshare import Skillshare

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    cookie = sys.argv[2]
    #trial
    print(cookie);
    ###
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""	 
                                                        
 #####  ###### #    # #       ####  ##### #    #  ####  
 #    # #      ##   # #      #    #   #   #    # #      
 #####  #####  # #  # #      #    #   #   #    #  ####  
 #    # #      #  # # #      #    #   #   #    #      # 
 #    # #      #   ## #      #    #   #   #    # #    # 
 #####  ###### #    # ######  ####    #    ####   ####  

   #####         #                                                        
 #     # #    # #    #    ##   #    # #    # #####  #    #   ##   #    # 
 # ### # #   #  #    #   #  #  ##   # #    # #    # #    #  #  #  #    # 
 # ### # ####   #    #  #    # # #  # #    # #####  ###### #    # #    # 
 # ####  #  #   ####### ###### #  # # #    # #    # #    # ###### #    # 
 #       #   #       #  #    # #   ## #    # #    # #    # #    #  #  #  
  #####  #    #      #  #    # #    #  ####  #####  #    # #    #   ##   
                                                                         
                                                        
				Visit Us for more Cool Stuff: https://forums.benlotus.com/

                """)


if __name__ == "__main__":
    info()
    main()
