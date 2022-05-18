local http = require('http')
local socket = require('socket')

local q = io.read()
wait(0.2)
file:read("./output.txt")
io.write("what title dumbass: ")

function test(url)
    url = "https://api.stemplayer.com/remixes"
    for _,v in next, url do 
        http.get('https://api.stemplayer.com/remixes')
        if http.response = 200 then
            return true
            print("stemplayer is online.")
        end
    end
end

test(url)
until true then 


local headers = {
    'Content-Type': 'application/json'
},

for i,v in ipairs(headers) do 
    http.post(headers, table.sort(headers, headers.__newindex(headers, i, v, [q])))))])
    return v
end
