const mongoose = require('mongoose');
const Schema = mongoose.Schema;

//Define schema for a member
const memberSchema = new Schema({
    membershipID: {
        type: String,
        required: true,
        unique: true,
        length: 10
    },
    traineeName: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    phoneNumber: {
        type: Number,
        required: true
    },
}, {
    timestamps: true
});

const Member = mongoose.model('Member', memberSchema);

module.exports = Member;