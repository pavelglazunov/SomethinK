class Validations {
    constructor() {
        const isNumeric = n => !isNaN(n);
    }

    validID(id) {
        return /^-?\d+$/.test(id);
    }

    validINT() {

    }

    validMSG() {

    }
}

//

function vld_integer(str, min_value = -1, max_length = 21) {
    return !((!parseInt(str)) || (parseInt(str) < min_value) || (str.length > max_length));
}