async function CheckPing(){
    document.getElementById("ping-btn").classList.toggle("is-loading")

    let table = document.getElementById("ping-table")
    table.tBodies[0].innerHTML = "";

    let pvp_worlds = [24,43,45,92,117]
    let ftp_worlds = [1,8,16,26,35,71,72,79,80,81,82,83,84,85,93,94,97,98,99,113,114,118,119,125,126,127,130,131,132,133,134,135,136,137,138,139,140,151,152,153,154,155,156,157,158,159,168,169,170,171,172,173,174,175,176,183,197,198,199,200,201,202,503,204,230]
    let worlds = await eel.CheckPing()()
    worlds = JSON.parse(worlds)
    
    worlds = worlds.reverse()

    for(let i = 0; i < worlds.length; i++){
        let w = worlds[i]
        let newRow = table.tBodies[0].insertRow(0)
        let worldCell = newRow.insertCell(0)
        let pingCell = newRow.insertCell(1)

        let message = ""

        if(pvp_worlds.includes(w.world - 300)){
            newRow.classList.add("has-text-danger")
            message = "PVP World! " + w.world
        }else if(ftp_worlds.includes(w.world - 300)){
            newRow.classList.add("has-text-warning")
            message = "F2P World " + w.world
        }else{
            newRow.classList.add("has-text-success")
            message = "Members World " + w.world
        }

        worldCell.innerText = message
        pingCell.innerText = w.ping
    }

    document.getElementById("ping-btn").classList.toggle("is-loading")
}