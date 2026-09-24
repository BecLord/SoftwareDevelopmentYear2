const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const Booking = require('../models/booking');

const bookingRouter = express.Router();


// View all bookings
bookingRouter.route('/')
  .get((req, res, next) => {
    Booking.find()
      .then((bookings) => {
        res.render('view-allbookings', { bookings, title: 'All Bookings - Rebel Performance' });
      })
      .catch((err) => next(err)); 
  })
  .post((req, res, next) => {
    res.statusCode = 403;
    res.end('POST operation not supported on /booking');
  })
  .put((req, res, next) => {
    res.statusCode = 403;
    res.end('PUT operation not supported on /booking');
  })
  .delete((req, res, next) => {
    res.statusCode = 403;
    res.end('DELETE operation not supported on /booking');
  });

// Create a new booking
bookingRouter.route('/new')
  .get((req, res, next) => {
    res.render('new-booking', { title: 'Create a New Booking' });
  })
  .post((req, res, next) => {
    const { traineeName, membershipID, className, trainingDate, cardNumber, expiryDate, securityCode } = req.body;

    const newBooking = new Booking({
      traineeName,
      membershipID,
      className,
      trainingDate,
      cardDetails: { cardNumber, expiryDate, securityCode }
    });

    newBooking.save()
      .then(() => {
        res.redirect('/booking');  
      })
      .catch((err) => next(err)); 
  });

//Find a Booking
bookingRouter.route('/find')
.get((req, res, next) => {
    res.render('find-booking', {title: 'Find a Booking'});
})
.post((req, res, next) => {
    console.log(req.body);
    Booking.find(req.body)
    .then((bookings) => {
        if (bookings.length > 0)
            res.render('view-allbookings', { bookings, title: 'Found Bookings'});
        else
            res.end('Sorry, no bookings found with the given details');
    })
    .catch((err) => next(err));
});

//Update Booking
bookingRouter.route('/update/:id')
  .get((req, res, next) => {
    const { id } = req.params;
    Booking.findById(id)
      .then((booking) => {
        if (booking) {
          res.render('update-booking', { title: 'Update Booking Details', booking });
        } else {
          res.status(404).send('Booking not found');
        }
      })
      .catch((err) => next(err));
  })
  .post((req, res, next) => {
    const { id } = req.params;
    Booking.findByIdAndUpdate(id, req.body, { new: true })
      .then((updatedBooking) => {
        if (updatedBooking) {
          res.redirect('/booking'); 
        } else {
          res.status(404).send('Booking not found');
        }
      })
      .catch((err) => next(err));
  });

  bookingRouter.route('/update_complete')
  .post((req, res, next) => {
    const { _id, traineeName, membershipID, className, trainingDate } = req.body;
    Booking.findByIdAndUpdate(_id, { traineeName, membershipID, className, trainingDate }, { new: true })
      .then(() => {
        res.redirect('/booking'); 
      })
      .catch((err) => next(err));
  });


//Delete a Booking
bookingRouter.route('/:id')
.post((req, res, next) => {
    const bookingId = req.params.id;

    Booking.findByIdAndDelete(bookingId)
      .then((deletedBooking) => {
        if (!deletedBooking) {
          const err = new Error('Booking not found');
          err.status = 404;
          return next(err);
        }
        res.redirect('/booking'); 
      })
      .catch((err) => next(err)); 
  });

module.exports = bookingRouter;
