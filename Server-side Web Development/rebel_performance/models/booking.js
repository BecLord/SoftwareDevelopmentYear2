const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Define the schema for a booking
const bookingSchema = new Schema({
    traineeName: {
        type: String,
        required: true
    },
    membershipID: {
        type: String,
        required: true,
        length: 10
    },
    className: {
        type: String,
        required: true
    },
    trainingDate: {
        type: Date,
        required: true
    },
    cardDetails: {
        cardNumber: {
            type: String,
            required: true
        },
        expiryDate: {
            type: String,
            required: true
        },
        securityCode: {
            type: String,
            required: true,
            length: 3
        }
    }
}, {
    timestamps: true 
});

const Booking = mongoose.model('Booking', bookingSchema);

module.exports = Booking;
