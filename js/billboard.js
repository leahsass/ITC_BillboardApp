var Billboard = {};


Billboard.newMessage = function () {
    $("#no-messages").hide();
    $("#add-message").hide();

    $("#new-msg-entry-form").show();
    $("#confirm-message").show();
    
};


Billboard.start = function () {
    $(document).ready(function () {
        $(".add-msg-btn").click(Billboard.newMessage);
        $("#new-msg-entry-form").hide();
        $("#confirm-message").hide();
    });
};


Billboard.start();