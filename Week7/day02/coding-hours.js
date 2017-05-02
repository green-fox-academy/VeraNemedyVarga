'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

var averageHours = 6;
var semesterLength = 17;
var workdaysInAWeek = 5;
var averageWorkHoursWeekly = 52;

var hoursSpentCoding = (averageHours * semesterLength * workdaysInAWeek);
console.log(hoursSpentCoding);

var percentageOfCodingHours = hoursSpentCoding * 100 / (averageWorkHoursWeekly * semesterLength);
console.log(percentageOfCodingHours);
