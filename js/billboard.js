var Billboard = {};


Billboard.newMessage = function () {
    $(".add-msg-btn").hide();

    $(".new-msg-entry-form").show();
    $(".btn-container").show();
    
};


Billboard.start = function () {
    $(document).ready(function () {
        $(".add-msg-btn").click(Billboard.newMessage);
        $(".new-msg-entry-form").hide();
        $(".btn-container").hide();
    });
};


Billboard.start();