const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const Booking = require('../models/booking');

const reportRouter = express.Router();

// Display report form for selecting the date range and trainee name
reportRouter.route('/')
  .get((req, res, next) => {
    res.render('report-form', { title: 'Generate Attendance Report' });
  })
  .post((req, res, next) => {
    const { startDate, endDate, traineeName } = req.body;
    const start = new Date(startDate);
    const end = new Date(endDate);

  // Ensure traineeName is provided
  if (!traineeName || traineeName.trim() === "") {
    return res.render('report-results', {
      title: 'Attendance Report',
      reportData: null,
      startDate: startDate,
      endDate: endDate,
      message: 'No trainee name provided. Please specify a trainee to generate a report.'
    });
  }

  let query = { traineeName: traineeName.trim() }; 

  console.log("Query:", query);
  console.log("Start Date:", start);
  console.log("End Date:", end);

  Booking.find(query)
    .then((bookings) => {
      // Filter bookings based on the date range
      const filteredBookings = bookings.filter((booking) => {
        const bookingDate = new Date(booking.trainingDate);
        return bookingDate >= start && bookingDate <= end;
      });

      // If no bookings are found for the specific trainee and date range
      if (filteredBookings.length === 0) {
        return res.render('report-results', {
          title: 'Attendance Report',
          reportData: null,
          startDate: startDate,
          endDate: endDate,
          message: 'No bookings found for the selected date range and trainee name.'
        });
      }

      res.render('report-results', {
        title: 'Attendance Report',
        reportData: filteredBookings,  
        startDate: startDate,
        endDate: endDate,
        message: null
      });
    })
    .catch((err) => {
      console.error("Error:", err);
      next(err);  
    });
});

module.exports = reportRouter;