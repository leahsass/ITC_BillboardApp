var Billboard = {};


Billboard.postMessage = function () {


};


Billboard.newMessage = function () {
    $("#no-messages").hide();
    $("#add-message").hide();

    $("#new-msg-entry-form").show();
    $("#confirm-message").show();

    $(".confirm-btn").click(Billboard.postMessage);
    
};


Billboard.start = function () {
    $(document).ready(function () {
        $(".add-msg-btn").click(Billboard.newMessage);
        $("#new-msg-entry-form").hide();
        $("#confirm-message").hide();
    });
};


Billboard.start();