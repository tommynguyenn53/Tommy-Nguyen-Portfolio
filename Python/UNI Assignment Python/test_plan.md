Author: Tommy Nguyen
SID: 530509598
Unikey: tong9587

**Test Cases**
Table 1. Summary of test cases for `buy_cheese` function in `shop.py`. 
| Test ID | Description            | Inputs   |          Expected Output        | Status |
| ------- | ---------------------- | ------   |          ---------------        | ------ |
| 01      |Valid amount of cheddar |test1(125)|Successfully purchase 1 cheddar. |  Pass  |
|         |cheese - Positive case  |cheddar 5 |50, (5, 0, 0)                    |        |        
|----------------------------------------------------------------------------------------|
| 02      |Valid amount of swiss   |test2(300)|Sucessfully purchase 2 swiss.    |  Pass  |
|         |- Positive case         |swiss 2   |200, (0, 0, 2)                   |        |
|----------------------------------------------------------------------------------------|
| 03      |Negative amount of      |test3(10) |Must purchase positive amount of |  Pass  |
|         |cheese - Negative case  |cheddar -1|cheese.                          |        |
|         |                        |          |0, (0, 0, 0)                     |        |
|----------------------------------------------------------------------------------------| 
| 04      |Purchasing brie cheese  |test4(50) |We don't see brie!               |  Pass  |
|         |- Negative case         |brie 5    |0, (0, 0, 0)                     |        |        
|----------------------------------------------------------------------------------------|
| 05      |Purchasing max amount of|test5(500)|Sucessfully purchase 50 cheddar. |  Pass  |
|         |marble cheese - Edge    |cheddar 50|500, (50, 0, 0)                  |        |        
|         |Case                    |          |                                 |        |
|----------------------------------------------------------------------------------------|
| 06      |Purchasing with 0 gold  |test6(0)  |Insufficient gold.               |  Pass  |
|         |- Edge Case.            |cheddar 1 |0, (0, 0, 0)                     |        |
|----------------------------------------------------------------------------------------|       


Table 2. Summary of test cases for `change_cheese` function in `game.py`.
| Test ID | Description            |                                            Inputs                                                      |                           Expected Output              | Status |
| ------- | ---------------------- | -------------------------------------------------------------------------------------------------------|--------------------------------------------------------|--------|
| 01      |Arming trap with all    | test1("info1110", "Cardboard and Hook Trap" ,  [["cheddar", 6], ["marble", 2], ["swiss", 4]], False)   | Do you want to arm your trap with Cheddar?             |  Pass  |            
|         |cheeses in inventory    | cheddar                                                                                                | Cardboard and Hook Trap is now armed with Cheddar      |        |
|         |- Positive case         | yes                                                                                                    | return True, cheddar                                   |        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 02      |Arming trap with one    | test2 ("info1110", "Cardboard and Hook Trap", [["cheddar", 1], ["marble", 0], ["swiss", 1]], False)    | Do you want to arm your trap with Swiss?               |  Pass  |
|         |swiss available         | swiss                                                                                                  | Cardboard and Hook Trap is now armed with swiss        |        |
|         |- Positive case         | yes                                                                                                    | return True, swiss                                     |        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 03      |Arming trap with        | test3("info1110", "Cardboard and Hook Trap", [["cheddar", -10], ["marble", 0], ["swiss", 0]], False)   | Out of cheese!                                         |  Pass  |
|         |negative cheese         | cheddar                                                                                                | return False, None                                     |        |
|         |available               |                                                                                                        |                                                        |        |
|         |- Negative case.        |                                                                                                        |                                                        |        | 
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 04      |Arming cheese that is   | test4("info1110", "Cardboard and Hook Trap", [["cheddar", 4], ["marble", 4], ["swiss", 4]], False)     | No such cheese!                                        |  Pass  |
|         |not available           | brie                                                                                                   | return False, None                                     |        |
|         |- Negative case         |                                                                                                        |                                                        |        |                                                
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 05      |Selecting available     | test5("info1110", "Cardboard and Hook Trap", [["cheddar", 10], ["marble", 10], ["swiss", 10]], False)  | Do you want to arm your trap with Marble?              |  Pass  |
|         |cheese but not arming it| marble                                                                                                 | return False, None                                     |        |
|         |- Edge case             | no                                                                                                     |                                                        |        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 06      |Arming trap with no     | test6("info1110", "Cardboard and Hook Trap", [["cheddar", 0], ["marble", 0], ["swiss", 0]], False)     | Out of cheese!                                         |  Pass  |
|         |cheese available.       | marble                                                                                                 | return False, None                                     |        |
|         |- Edge case             |                                                                                                        |                                                        |        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|


    
