
$("#cupcake-form").on("submit", async function addcupcake(evt){
    evt.preventDefault()
    let flavor = $("#txt-flavor").val()
    let size = $("#txt-size").val()
    let rating = $("#txt-rating").val()
    let image = $("#txt-image").val()


    const response = await axios.post("http://127.0.0.1:5000/api/cupcakes", 
    params = {
        "flavor":flavor,
        "size":size,
        "rating":rating,
        "image":image
        
    })

    let newcupcake = $(generateNewTr(response.data.cupcake))
    $("#table-load").append(newcupcake)

    $("#form_add").hide()

})

$('#table-load').on("click",".delete-cupcake",async function(evt){

    evt.preventDefault()
    const $tr = $(evt.target).closest('tr')
    const id = $tr.attr('id')

    await axios.delete(`http://127.0.0.1:5000/api/cupcakes/${id}`)
    $(this).parent().remove()  
})

async function get_cupcakes(){
    
    
    const response= await axios({
        url: 'http://127.0.0.1:5000/api/cupcakes',
        method: "GET",
      });
        
      for(let cupcake of response.data.cupcakes){
          let newcupcake = $(generateNewTr(cupcake))
          $("#table-load").append(newcupcake)

      }

}

function generateNewTr(cupcake){
    return `<tr id = ${cupcake.id}><td><img src=${cupcake.image} height="200px" width="200px"></img>
    <P><a href=''>${cupcake.flavor}</a></P>
    <h3>Rating:${cupcake.rating}, Size:${cupcake.size}</h3>
    <button class="delete-cupcake" id="${cupcake.id}">X</button>`;
}

$('.display-form').click(function addForm(){
    $("#form_add").show()
})

  
 $(get_cupcakes())