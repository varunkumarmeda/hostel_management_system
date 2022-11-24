

DROP TABLE IF EXISTS `Hostel`;
CREATE TABLE `Hostel` (
  `Hostel_id` int(10) NOT NULL AUTO_INCREMENT,
  `Hostel_name` varchar(255) NOT NULL,
  `current_no_of_rooms` varchar(255) DEFAULT NULL,
  `No_of_rooms` int DEFAULT NULL,
  `No_of_students` int DEFAULT NULL,
  PRIMARY KEY (`Hostel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;


--
-- Table structure for table `Hostel_Manager`
--

DROP TABLE IF EXISTS `Hostel_Manager`;

CREATE TABLE `Hostel_Manager` (
  `Hostel_man_id` int(10) NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Mob_no` varchar(255) NOT NULL,
  `Hostel_id` int(10) NOT NULL,
  `Pwd` LONGTEXT NOT NULL,
  `Isadmin` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`Hostel_man_id`),
  UNIQUE (`Username`),
  KEY `Hostel_id` (`Hostel_id`),
  FOREIGN KEY (`Hostel_id`) REFERENCES `Hostel` (`Hostel_id`)
);


--
-- Table structure for table `Room`
--

DROP TABLE IF EXISTS `Room`;

CREATE TABLE `Room` (
  `Room_id` int(10) NOT NULL AUTO_INCREMENT,
  `Hostel_id` int(10) NOT NULL,
  `Room_No` int(10) NOT NULL,
  `Allocated` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`Room_id`),
  KEY `Hostel_id` (`Hostel_id`),
  FOREIGN KEY (`Hostel_id`) REFERENCES `Hostel` (`Hostel_id`)
) ;



-- tABLE STRUCTURE FOR FURNITURE

CREATE TABLE FURNITURE (    
    Hostel_id int,
    Room_id int(10) NOT NULL,
    Furniture_id int NOT NULL,
    Furniture_TYPE varchar(30),
    PRIMARY KEY (Furniture_id),
    FOREIGN KEY (Hostel_id) REFERENCES Hostel(Hostel_id),
    FOREIGN KEY (Room_id) REFERENCES Room(Room_id)
);


-- Table structure for table `Student`
--

DROP TABLE IF EXISTS `Student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Student` (
  `Student_id` varchar(255) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `Lname` varchar(255) NOT NULL,
  `Mob_no` varchar(255) NOT NULL,
  `Dept` varchar(255) NOT NULL,
  `Year_of_study` varchar(255) NOT NULL,
  `Hostel_id` int(10) DEFAULT NULL,
  `Room_id` int(10) DEFAULT NULL,
  PRIMARY KEY (`Student_id`),
  KEY `Hostel_id` (`Hostel_id`),
  KEY `Room_id` (`Room_id`),
  FOREIGN KEY (`Hostel_id`) REFERENCES `Hostel` (`Hostel_id`) on  delete  cascade on  update cascade,
  FOREIGN KEY (`Room_id`) REFERENCES `Room` (`Room_id`) on  delete  cascade on update  cascade 
) ;

-- tABLE STRUCTURE FOR VISITOR TABLE

CREATE TABLE VISITOR(
    VISITOR_ID INT NOT NULL,
    IN_TIME DATETIME,
    OUT_TIME DATETIME,
    NAME VARCHAR(20),
    Student_id VARCHAR(20),
    PRIMARY KEY  (VISITOR_ID),
    FOREIGN KEY (Student_id) REFERENCES STUDENT(Student_id) 
);



INSERT INTO `Hostel` VALUES (1,'MM BLOCK',NULL,50,NULL),
(2,'IH BLOCK',NULL,52,NULL),
(3,'IT BLOCK',NULL,45,NULL),
(4,'MESS BLOCK',NULL,40,NULL),
(5,'NEW BLOCK',NULL,25,NULL),
(6,'NBX',NULL,20,NULL);

INSERT INTO Hostel_Manager VALUES (100,'M_REDDY','MAHESH','REDDY','9871234560',1,'helloworld',DEFAULT),
(101,'B_REDDY','BABU','REDDY','9813234560',2,'helloworld1',DEFAULT),
(102,'K_REDDY','KIRAN','REDDY','9845634560',3,'helloworld2',DEFAULT),
(103,'R_REDDY','RAKESH','REDDY','9789234560',4,'helloworld3',DEFAULT),
(104,'K_KIRAN','KIRAN','KUMAR','9852634560',5,'helloworld4',DEFAULT),
(105,'S_GUPTHA','SAFAL','GUPTHA','9963234560',5,'helloworld5',DEFAULT);

INSERT INTO Room VALUES (5600,1,01,DEFAULT),
(5645,2,01,1),
(5663,3,03,DEFAULT),
(5644,4,02,1),
(5633,5,03,DEFAULT),
(5689,6,02,1);

INSERT INTO FURNITURE VALUES (1,5600,10001,'AC'),
(2,5645,10002,'AC WITH BED'),
(3,5663,10003,'NON AC'),
(4,5644,10004,'NON AC WITH BED'),
(5,5633,10005,'ATTACHED BT'),
(6,5689,10006,'AC WITH ATTACHED BT');

INSERT INTO STUDENT VALUES(250,'SURYA','TEJA','9873214560','CSE',2024,1,5600),
(251,'VARUN','KUMAR','7337265192','CSE',2024,2,5645),
(252,'AJAY','DEVAGAN','6937265192','ECE',2024,3,5663),
(253,'PRADEEP','KUMAR','9637265192','CSE',2024,4,5645),
(254,'NILESH','KUMAR','6397265192','ECE',2024,5,5633),
(255,'SUNDEEP','A','9667265192','CSE',2024,6,5689);

INSERT INTO VISITOR VALUES(661,'2022-06-18 10:34:09','2022-06-18 11:34:09','VIJAY KUMAR',251);
-- JOINS
-- LEFT JOIN
-- list all the hostel manager details with the number of students in that particular block they are administrating for
SELECT *
FROM Hostel
LEFT JOIN Hostel_Manager
ON Hostel.Hostel_id = Hostel_Manager.Hostel_id;



SELECT *
FROM Hostel
RIGHT JOIN Hostel_Manager
ON Hostel.Hostel_id = Hostel_Manager.Hostel_id;
-- INNER JOIN
SELECT *
FROM STUDENT
INNER JOIN VISITOR
ON STUDENT.Student_id = VISITOR.Student_id;
-- SELF JOIN
SELECT A.Room_id AS ROOM_1, B.Room_id AS ROOM_2, A.room_no
FROM Room A,Room B 
WHERE A.ROOM_ID <> B.Room_id;

--- aggrigate functions
-- average number of rooms in the block
SELECT AVG(No_of_rooms) AS avg_no_of_rooms_in_the_block
FROM hostel;

-- number of visitors on a particular dateawwd
seleCt DATE(IN_TIME),count(VISITOR_ID)
FROM VISITOR
GROUP BY date(IN_TIME);
-- NO OF STUDENTS STAYING IN THE HOSTEL
SELECT COUNT(Student_id) AS NUMBER_OF_STUDENTS
FROM STUDENT;
-- SUM OF STUDENTS THE HOSTEL CAN ACCOMIDATE
SELECT SUM(No_of_students)
FROM HOSTEL;

-- functions 

DELIMITER $$
CREATE FUNCTION rooms(No_of_rooms int)
	RETURNS varchar(100)
	DETERMINISTIC
	BEGIN
    if No_of_rooms>42 THEN
    	RETURN ('Rooms are filling fast');
    ELSE
    	RETURN ('Rooms are yet to be filled');
    END if;
    END $$
    DELIMITER ;
-- CALLING THE FUNCTION
--SELECT Hostel_name,rooms(No_of_rooms) AS COMMENTS FROM hostel;


-- PROCEDURE
DELIMITER $$
CREATE PROCEDURE STUDENTS_IN_HOSTEL(IN X INT)
	BEGIN
    SELECT * FROM STUDENT WHERE STUDENT_ID = X;
    END $$
DELIMITER ;
CALL STUDENTS_IN_HOSTEL(250);

-- TRIGGER
DELIMITER //
CREATE TRIGGER hostel_insertion
BEFORE INSERT
ON HOSTEL FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
SET error_msg = ('CAN HAVE MAXIMUM OF 60 ROOMS');

IF (New.No_of_rooms ) > 60 
THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg; 
END IF;
END //
DELIMITER ;

-- INSERT INTO `Hostel` VALUES (8,'MM BLOCK',NULL,65,NULL);
-- CURSOR
create table student_backup ( STUD_ID varchar(6), 
f_name varchar(30),
L_NAME varchar(16),
MOBILE_NUMBER Varchar(10) ,
DEPARTMENT varchar(6),
GRADUATION_YEAR varchar(6),
H_ID varchar(6),
ROOM_ID varchar(6));


DELIMITER //
CREATE PROCEDURE cursor_1()
   BEGIN
      DECLARE done INT DEFAULT 0;
      DECLARE A,B,C,D,E,F,G,H VARCHAR(30);
      DECLARE cur CURSOR FOR SELECT * FROM STUDENT;
      DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
      OPEN cur;
      label: LOOP
      FETCH cur INTO A,B,C,D,E,F,G,H;
      INSERT INTO student_backup VALUES(A,B,C,D,E,F,G,H);
      IF done = 1 THEN LEAVE label;
      END IF;
      END LOOP;
      CLOSE cur;
   END//
DELIMITER ;

call cursor_1();