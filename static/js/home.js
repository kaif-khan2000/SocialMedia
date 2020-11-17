var id = -1;
var next = 0;
var friendslist = document.getElementById("friendsList")
var postdiv = document.getElementById("postfromajax")
function fetchPost() {
    $.ajax({
        type: "GET",
        url: '/fetchPost',
        data: {
            'next': next,
        },
        success: function (response) {
            
            for (i in response) {
                color = 'black;'
                if (response[i].like) {
                    color = "#0056b3;"
                }
                time = response[i].timestamp
                time = time.substring(0, 16)
                if (response[i].media_type == "image") {
                    postdiv.innerHTML += '<div class="c-inner-profile-tile">' +
                        '<div class="profile-header">' +
                        ' <div class="img-section">' +
                        '  <img src="' + response[i].profile_pic + '" alt="" />' +
                        ' </div>' +
                        ' <div class="user-details">' +
                        '     <p>' + response[i].name + '</p>' +
                        '     <p>' + time + '</p>' +
                        ' </div>' +
                        '</div>' +
                        '<hr>' +
                        '<div style="font-size: 23px; margin-left:20px;">' +
                        '     <p>' + response[i].desc + '</p>' +
                        '</div>' +
                        '<div class="c-post" style="">' +
                        '<img src="' + response[i].media + '" alt="" />' +
                        '</div>' +

                        // <video width="400" controls style="padding-left: 4px;">
                        //     <source src="'+response[i].media+'">
                        //     Your browser does not support HTML video.
                        // </video>

                        '<hr>' +
                        '<div class="c-post-details">' +
                        '  <div class="c-user-like">' +
                        '    <a href="javascript:manageLike(' + response[i].id + ')">' +
                        '        <i class="fas fa-thumbs-up" id="likecolor-' + response[i].id + '" style="color:' + color + '"> </i>' +
                        '    </a>' +
                        '    <p id="no_of_likes_' + response[i].id + '">' + response[i].no_of_likes + '</p>' +
                        ' </div>' +
                        ' <!-- BUTTON POPUP 4 -->' +
                        '<button data-toggle="modal" data-target="#comment-popup" id="comments-' + response[i].id + '"' +
                        '   onclick="loadComments(' + response[i].id + ')">' +
                        '  <i class="fas fa-comment"></i>' +
                        '</button>' +

                        '<button data-toggle="modal" data-target="#share-post">' +
                        ' <i class="fas fa-share"></i>' +
                        '</button>' +
                        '</div>' +
                        ' </div>';
                } else if (response[i].media_type == "video") {
                    postdiv.innerHTML += '<div class="c-inner-profile-tile">' +
                        '<div class="profile-header">' +
                        ' <div class="img-section">' +
                        '  <img src="' + response[i].profile_pic + '" alt="" />' +
                        ' </div>' +
                        ' <div class="user-details">' +
                        '     <p>' + response[i].name + '</p>' +
                        '     <p>' + time + '</p>' +
                        ' </div>' +
                        '</div>' +
                        '<hr>' +
                        '<div style="font-size: 23px; margin-left:20px;">' +
                        '     <p>' + response[i].desc + '</p>' +
                        '</div>' +
                        // '<div class="c-post" style="">' +
                        // '<img src="' + response[i].media + '" alt="" />' +
                        // '</div>' +

                        '<video width="400" controls style="padding-left: 4px;">' +
                        '   <source src="' + response[i].media + '">' +
                        '  Your browser does not support HTML video.' +
                        '</video>' +

                        '<hr>' +
                        '<div class="c-post-details">' +
                        '  <div class="c-user-like">' +
                        '    <a href="javascript:manageLike(' + response[i].id + ')">' +
                        '        <i class="fas fa-thumbs-up" id="likecolor-' + response[i].id + '" style="color:' + color + '"> </i>' +
                        '    </a>' +
                        '    <p id="no_of_likes_' + response[i].id + '">' + response[i].no_of_likes + '</p>' +
                        ' </div>' +
                        ' <!-- BUTTON POPUP 4 -->' +
                        '<button data-toggle="modal" data-target="#comment-popup" id="comments-' + response[i].id + '"' +
                        '   onclick="loadComments(' + response[i].id + ')">' +
                        '  <i class="fas fa-comment"></i>' +
                        '</button>' +

                        '<button data-toggle="modal" data-target="#share-post">' +
                        ' <i class="fas fa-share"></i>' +
                        '</button>' +
                        '</div>' +
                        ' </div>';
                } else {
                    postdiv.innerHTML += '<div class="c-inner-profile-tile">' +
                        '<div class="profile-header">' +
                        ' <div class="img-section">' +
                        '  <img src="' + response[i].profile_pic + '" alt="" />' +
                        ' </div>' +
                        ' <div class="user-details">' +
                        '     <p>' + response[i].name + '</p>' +
                        '     <p>' + time + '</p>' +
                        ' </div>' +
                        '</div>' +
                        '<hr>' +
                        '<div style="font-size: 23px; margin-left:20px;">' +
                        '     <p>' + response[i].desc + '</p>' +
                        '</div>' +
                        // '<div class="c-post" style="">' +
                        // '<img src="' + response[i].media + '" alt="" />' +
                        // '</div>' +

                        // <video width="400" controls style="padding-left: 4px;">
                        //     <source src="'+response[i].media+'">
                        //     Your browser does not support HTML video.
                        // </video>

                        '<hr>' +
                        '<div class="c-post-details">' +
                        '  <div class="c-user-like">' +
                        '    <a href="javascript:manageLike(' + response[i].id + ')">' +
                        '        <i class="fas fa-thumbs-up" id="likecolor-' + response[i].id + '" style="color:' + color + '"> </i>' +
                        '    </a>' +
                        '    <p id="no_of_likes_' + response[i].id + '">' + response[i].no_of_likes + '</p>' +
                        ' </div>' +
                        ' <!-- BUTTON POPUP 4 -->' +
                        '<button data-toggle="modal" data-target="#comment-popup" id="comments-' + response[i].id + '"' +
                        '   onclick="loadComments(' + response[i].id + ')">' +
                        '  <i class="fas fa-comment"></i>' +
                        '</button>' +

                        '<button data-toggle="modal" data-target="#share-post">' +
                        ' <i class="fas fa-share"></i>' +
                        '</button>' +
                        '</div>' +
                        ' </div>';
                }
            }
            next++;

        }
    });
}


function fetchFriends() {
    $.ajax({
        type: 'GET',
        url: '/friendsList',
        async:false,
        success: function (response) {
            friendslist.innerHTML = ""
            for (i in response) {
                console.log(response[i].fields);
                img = response[i].fields.profile_pic
                if (img == "") {
                    img = 'static/img/profile_pic.png'
                }
                friendslist.innerHTML += '<a href="">' +
                    '<div class="friend-tile">' +
                    '<div class="c-image-square">' +
                    '<img src="' + img + '" alt="" />' +
                    '</div>' +
                    '<p>' + response[i].fields.name + '</p>' +
                    ' </div>' +
                    '</a>';
            }
        }
    });
}
fetchFriends();
fetchPost();
var next = 0;
function loadComments(kid) {
    id = kid;
    console.log("activated")
    var comments = document.getElementById('comments2')
    
    comments.innerHTML = '';
    
    $.ajax({
        type: "GET",
        url: "/loadComments",
        data: {
            'id': id,
            'next': next,
        },
        success: function (response) {
            console.log(response)
            for (i in response) {
                time = response[i].timeStamp;
                time = time.substring(0, 16)
                comments.innerHTML += ' <div class="c-comment-tile-header">'
                    + '<img src="' + response[i].profile_pic + '" alt=""'
                    + ' style="width: 30px; height: 30px; border-radius: 100%; margin-right: 10px" />'
                    + ' <p><b><i>' + response[i].name + ' {' + time + '}</i></b></p>'
                    + '</div>'
                    + '<div class="c-comment-tile-body">'
                    + response[i].comment
                    + '</div>'
            }
        }

    });
}

function addComment(stat) {
    var comment = document.getElementById('commentbox')
    var comments = document.getElementById('comments2')
    if (stat == 'clear') {
        comments.innerHTML = '';
        return;
    }
    if (comment.value == '') return;
    $.ajax({
        type: "GET",
        url: "/addComment",
        data: {
            'id': id,
            'comment': comment.value,
        },
        success: function (response) {
            comment.value = '';
            loadComments(id);
        }

    });
}


function manageLike(kid) {
    var likecolor = document.getElementById('likecolor-' + kid)
    var stat = '';
    var no_of_likes = document.getElementById('no_of_likes_' + kid)
    if (likecolor.getAttribute('style') == "color:black;") {
        likecolor.setAttribute('style', "color: #0056b3;");
        stat = 'add';
    } else {
        likecolor.setAttribute('style', 'color:black;');
        stat = 'remove';
    }

    $.ajax({
        type: "GET",
        url: '/' + stat + 'Like',
        data: {
            'id': kid,
            'stat': stat
        },
        success: function (response) {
            no_of_likes.innerHTML = response.no_of_likes
        }
    });
}

