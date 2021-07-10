
## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Booking flow
* greet
  - utter_greet
  - utter_booking
* affirm
  - utter_display_MovieList
* user_choose_Movie
  - utter_display_type_of_seat
* user_choose_type_of_seat
  - utter_ask_for_num_of_seat
* user_entered_total_num_of_seat
  - send_total
  - utter_enjoy

## Dont want to book
* greet
  - utter_greet
  - utter_booking
* deny
  - utter_goodbye
