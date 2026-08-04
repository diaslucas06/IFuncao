interface ConfComp {
    children: React.ReactNode,
    tamanho?: number
}

export function ConfDiv({children}:ConfComp) {
    return (
        <div className="flex flex-col py-12 px-20 gap-7">
            {children}
        </div>
    )
}

export function ConfH1({children}:ConfComp) {
    return (
        <h1 className="font-bold text-[48px]">
            {children}
        </h1>
    )
}

export function ConfH2({children}:ConfComp) {
    return (
        <h2 className="font-bold text-[36px]">
            {children}
        </h2>
    )
}

export function ConfP({children}:ConfComp) {
    return (
        <p className="font-poppins-sans text-[24px]">
            {children}
        </p>
    )
}

export function ConfCard({children, tamanho}:ConfComp) {
    return (
        <div className="flex flex-col gap-5 bg-(--settings-card-color) rounded-4xl shadow-lg p-10" style={{ width: `${tamanho}%` }}>
            {children}
        </div>
    )
}

export function ConfLi({children}:ConfComp) {
    return (
        <li className="flex flex-col justify-between text-[20px] p-5">
            {children}
        </li>
    )
}

export function ConfNotificacoesText({children}:ConfComp) {
    return (
        <p className="font-poppins-sans text-[32px]">
            {children}
        </p>
    )
}

export function ConfInfoLi({children}:ConfComp) {
    return (
        <li className="text-[24px] font-poppins-sans">
            {children}
        </li>
    )
}