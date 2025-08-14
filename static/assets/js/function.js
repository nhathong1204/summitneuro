$(document).ready(function() {
    $(document).on("submit","#contact-form-ajax",function(e){
        e.preventDefault()
        console.log("Submited...")
        let full_name = $("#full_name").val()
        let email = $("#email").val()
        let phone = $("#phone").val()
        let subject = $("#subject").val()
        let message = $("#message").val()
        console.log(full_name, email, phone, subject, message)

        $.ajax({
            url: "/ajax-contact-form",
            data: {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "subject": subject,
                "message": message,
            },
            dataType: "json",
            success: function(res) {
                console.log("Sent data to server...")
                if(res.success == true) {
                    alert("Email sent successfully!")
                    location.reload();
                }
            }
        })
    })
})