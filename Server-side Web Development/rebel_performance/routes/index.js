const express = require('express');
const router = express.Router();
const trainingClasses = require('../training_classes.json');

// Home page route
router.get('/', function(req, res, next) {
    console.log('Training Classes:', trainingClasses.training_classes);
    res.render('index', { title: 'Rebel Performance', 
        trainingClasses: trainingClasses.training_classes
    });
});

// About Us page route
router.get('/about', (req, res) => {
    console.log('Training Classes:', trainingClasses.training_classes);
    res.render('about', {title: 'About Rebel Performance',
        trainingClasses: trainingClasses.training_classes
    });
});

//Help page route
router.get('/help', (req, res) => {
    res.render('help', {title: 'Help & Support'});
})


module.exports = router;
