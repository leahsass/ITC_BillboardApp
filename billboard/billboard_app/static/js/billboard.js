var Billboard = {};



Billboard.newMessage = function () {
    $("#no-messages").hide();
    $("#add-message").hide();

    $("#new-msg-entry-form").show();
    $("#confirm-message").show();

    $(".cancel-btn").click(Billboard.cancelMessage);
    
};



Billboard.cancelMessage = function () {
    $("#add-message").show();
    $(".add-msg-btn").click(Billboard.newMessage);
    $("#new-msg-entry-form").hide();
    $("#confirm-message").hide();
};



Billboard.start = function () {
    $(document).ready(function () {
        $(".add-msg-btn").click(Billboard.newMessage);
        $("#new-msg-entry-form").hide();
        $("#confirm-message").hide();
    });
};



Billboard.start();