function send_msg(msg_to_send){
    let ajax= new XMLHttpRequest();
    ajax.open('POST','/chat');
    ajax.setRequestHeader("Content-Type", "application/json");
    ajax.send(JSON.stringify(msg_to_send));
    ajax.onreadystatechange = function() {
        if (ajax.readyState === 4 && ajax.status === 200) {
            console.log('responseText:' + ajax.responseText);
            try {
                var data = JSON.parse(ajax.responseText);
            }
            catch(err) {
                console.log(err.message + " in " + ajax.responseText); return;
            }
            create_card(data);
        }
        else{
            if(ajax.readyState === 4){
                on_error(data);
            }
        }
    };
}
function create_card(data,user=false){
    let classes='card-subtitle mb-2 text-muted text-';
    let choice='';
    if(user) {
        choice='right';
        classes+='right'
    }
    else {
        choice='left';
        classes+='left';
    }
    let card='<div class="card"><div class="card-body"><h6 class="'+classes+'">'+
    data['name']+
    '</h6><p class="card-text float-'+choice+'">'+data['msg']+'</p></div></div>'
    document.getElementById('msg_block').insertAdjacentHTML("beforeend", card);
}
function on_success(data){
    create_card(data)
}
function on_error(data){
    console.log('error'+data);
}

function update_msg(event) {
    let key = event.key;

    // If the user has pressed enter
    if (key === 'Enter') {
		el=document.getElementById('input_box');
        let user_msg=el.value;
	 	el.value='';
		create_card({'name':'You','msg':user_msg},true)
	 	send_msg({'handle':'You','msg':user_msg});
    }
    else {
        return false;
    }
}