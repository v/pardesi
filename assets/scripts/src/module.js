module.exports = function() {
    var something = function() {
        console.log("something");
    };
    return {
        something: something,
    };
}();
