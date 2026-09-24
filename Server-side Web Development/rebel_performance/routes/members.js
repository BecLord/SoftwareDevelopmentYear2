const express = require('express');
const Member = require('../models/member');  
const router = express.Router();

//Member login
router.route('/login')
  .get((req, res) => {
    res.render('login', { title: 'Login to Rebel Performance' });
  })
  .post((req, res, next) => {
    const { membershipID } = req.body;

    
    Member.findOne({ membershipID })
      .then((member) => {
        if (!member) {
          return res.redirect('/members/signup');
        } else {
          res.render('member-profile-booking', {
            title: 'Member Profile and Bookings',
            member: member
          });
        }
      })
      .catch(next);  
  });

  //Member signup
router.route('/signup')
  .get((req, res) => {
    res.render('signup', { title: 'Become a Member of Rebel Performance' });
  })
  .post((req, res, next) => {
    const { membershipID, traineeName, email, phoneNumber } = req.body;

    Member.findOne({ membershipID })
      .then((existingMember) => {
        if (existingMember) {
          const err = new Error('A member with this Membership ID already exists!');
          err.status = 403;
          return next(err);
        }

        return Member.create({
          membershipID,
          traineeName,
          email,
          phoneNumber
        });
      })
      .then((newMember) => {
        res.render('member-profile-booking', {
          title: 'Member Profile and Bookings',
          member: newMember
        });
      })
      .catch(next);  
  });

// Render profile page for a member
router.route('/profile/:id')
  .get((req, res, next) => {
    const { id } = req.params;
    Member.findById(id)
      .then((member) => {
        if (member) {
          res.render('profile', { title: 'Member Profile', member });
        } else {
          res.status(404).send('Member not found');
        }
      })
      .catch(next);
  });

// Update member details 
router.route('/update/:id')
  .get((req, res, next) => {
    const { id } = req.params;
    Member.findById(id)
      .then((member) => {
        if (member) {
          res.render('update-member', { title: 'Update Member Details', member });
        } else {
          res.status(404).send('Member not found');
        }
      })
      .catch(next);
  })
  .post((req, res, next) => {
    const { id } = req.params;
    const { membershipID, traineeName, email, phoneNumber } = req.body;

    Member.findByIdAndUpdate(id, {
      membershipID,
      traineeName,
      email,
      phoneNumber
    })
      .then(() => {
        res.redirect(`/members/profile/${id}`);
      })
      .catch(next);
  });

// Delete a member
router.route('/delete/:id')
  .post((req, res, next) => {
    const { id } = req.params;

    Member.findByIdAndDelete(id)
      .then((deletedMember) => {
        if (deletedMember) {
          res.redirect('/members/login');  
        } else {
          const err = new Error('Member not found');
          err.status = 404;
          return next(err);
        }
      })
      .catch(next);
  });

module.exports = router;
