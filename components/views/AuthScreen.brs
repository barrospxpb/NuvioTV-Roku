sub init()
    m.leftTitle = m.top.findNode("leftTitle")
    m.leftDesc = m.top.findNode("leftDesc")
    m.leftHint = m.top.findNode("leftHint")
    m.cardTitle = m.top.findNode("cardTitle")
    m.cardSub = m.top.findNode("cardSub")
    m.qrImage = m.top.findNode("qrImage")
    m.qrSpin = m.top.findNode("qrSpin")
    m.codeText = m.top.findNode("codeText")
    m.siteText = m.top.findNode("siteText")
    m.statusText = m.top.findNode("statusText")
    m.terms = m.top.findNode("terms")
    m.buttonsGroup = m.top.findNode("buttons")
    m.cardTitle.font.size = 46
    m.cardSub.font.size = 30
    m.statusText.font.size = 28
    m.terms.font.size = 24
    m.codeText.font.size = 34
    m.siteText.font.size = 24
    m.qrSpin.poster.uri = "pkg:/images/spinner.png"
    m.qrSpin.poster.width = 96
    m.qrSpin.poster.height = 96
    m.qrSpin.poster.blendColor = "0x0D0D0DFF"
    m.index = 0
    m.buttons = []
    m.qrImage.observeField("loadStatus", "onQrStatus")
    render()
end sub

sub render()
    m.cardTitle.text = "Conectar à conta"
    m.cardSub.text = "Escaneie o QR Code com seu celular"
    m.terms.text = "Ao entrar, você concorda com os Termos do Nuvio."
    defs = [{ id: "refresh", label: "Novo QR" }]
    if m.top.mode = "onboarding"
        defs.Push({ id: "skip", label: "Continuar sem conta" })
    else
        defs.Push({ id: "back", label: "Voltar" })
    end if
    buildButtons(defs)
    onHint()
end sub

sub buildButtons(defs as object)
    m.buttonsGroup.removeChildrenIndex(m.buttonsGroup.getChildCount(), 0)
    m.buttons = []
    widths = [242, 414]
    gap = 18
    x = 100
    for i = 0 to defs.Count() - 1
        g = m.buttonsGroup.createChild("Group")
        g.translation = [x, 0]
        bg = g.createChild("Poster")
        bg.uri = "pkg:/images/legacy_login_button_dark.png"
        bg.width = widths[i]
        bg.height = 76
        label = g.createChild("Label")
        label.font = "font:MediumSystemFont"
        label.font.size = 30
        label.width = widths[i]
        label.height = 76
        label.horizAlign = "center"
        label.vertAlign = "center"
        label.text = defs[i].label
        m.buttons.Push({ id: defs[i].id, bg: bg, label: label })
        x = x + widths[i] + gap
    end for
    if m.index >= m.buttons.Count() then m.index = 0
    paint()
end sub

sub paint()
    for i = 0 to m.buttons.Count() - 1
        b = m.buttons[i]
        if i = m.index
            b.bg.uri = "pkg:/images/legacy_login_button_white.png"
            b.label.color = "0x0D0D0DFF"
        else
            b.bg.uri = "pkg:/images/legacy_login_button_dark.png"
            b.label.color = "0xFFFFFFFF"
        end if
    end for
end sub

sub onQr()
    url = m.top.qr
    m.siteText.text = ""
    if url = ""
        m.qrImage.uri = ""
        m.qrSpin.visible = true
        m.qrSpin.control = "start"
        return
    end if
    if Instr(1, url, "nuvio.tv") > 0 then m.siteText.text = "nuvio.tv/link"
    m.qrImage.uri = "https://api.qrserver.com/v1/create-qr-code/?size=420x420&margin=0&data=" + url.EncodeUriComponent()
end sub

sub onQrStatus()
    if m.qrImage.loadStatus = "ready" or m.qrImage.loadStatus = "failed"
        m.qrSpin.visible = false
        m.qrSpin.control = "stop"
    end if
end sub

sub onCode()
    if m.top.code = ""
        m.codeText.text = ""
    else
        m.codeText.text = "Código: " + m.top.code
    end if
end sub

sub onStatus()
    m.statusText.text = m.top.status
end sub

sub onHint()
    ' This UI intentionally starts without addon/account claims. Guest is clean.
    m.leftHint.text = ""
end sub

function onKeyEvent(key as string, press as boolean) as boolean
    if not press then return true
    if key = "left" and m.index > 0
        m.index = m.index - 1
        paint()
    else if key = "right" and m.index < m.buttons.Count() - 1
        m.index = m.index + 1
        paint()
    else if key = "OK" and m.index < m.buttons.Count()
        m.top.event = { type: m.buttons[m.index].id }
    else if key = "back"
        if m.top.mode = "onboarding" then m.top.event = { type: "exit" } else m.top.event = { type: "back" }
    end if
    return true
end function
