## happy path 1 (C:\Users\Yash\AppData\Local\Temp\tmpumrf2qtq\7064964b38064349b87a27b37f25a6fe_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_booking -->
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->


## happy path 2 (C:\Users\Yash\AppData\Local\Temp\tmpumrf2qtq\7064964b38064349b87a27b37f25a6fe_conversation_tests.md)
* greet: hello there!
    - utter_greet
    - action_listen   <!-- predicted: utter_booking -->
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\Yash\AppData\Local\Temp\tmpumrf2qtq\7064964b38064349b87a27b37f25a6fe_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_booking -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_display_MovieList -->


## sad path 2 (C:\Users\Yash\AppData\Local\Temp\tmpumrf2qtq\7064964b38064349b87a27b37f25a6fe_conversation_tests.md)
* greet: hello
    - utter_greet
    - action_listen   <!-- predicted: utter_booking -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye


## sad path 3 (C:\Users\Yash\AppData\Local\Temp\tmpumrf2qtq\7064964b38064349b87a27b37f25a6fe_conversation_tests.md)
* greet: hi
    - utter_greet
    - action_listen   <!-- predicted: utter_booking -->
* mood_unhappy: very terrible   <!-- predicted: goodbye: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye


