interface ConfComp {
    children: React.ReactNode,
    tamanho?: number,
    className?: string
}

export function ConfDiv({children}:ConfComp) {
    return (
        <div className="flex flex-col w-full py-5 px-5 gap-5 md:gap-7 md:py-10 md:px-10 lg:py-10 lg:px-10 lp:py-10 lp:px-15 pc:py-12 pc:px-20">
            {children}
        </div>
    )
}

export function ConfH1({children}:ConfComp) {
    return (
        <h1 className="font-bold text-[24px] text-center md:text-start md:text-[28px] lg:text-[32px] lp:text-[40px] pc:text-[48px]">
            {children}
        </h1>
    )
}

export function ConfH2({children}:ConfComp) {
    return (
        <h2 className="font-bold text-[20px] md:text-[24px] lg:text-[28px] lp:text-[32px] pc:text-[36px]">
            {children}
        </h2>
    )
}

export function ConfP({children}:ConfComp) {
    return (
        <p className="font-poppins-sans lg:text-[20px] pc:text-[24px]">
            {children}
        </p>
    )
}

export function ConfCard({children, tamanho, className}:ConfComp) {
    return (
        <div className={`flex flex-col bg-(--settings-card-color) rounded-4xl shadow-lg p-5 gap-2 md:p-6 lg:p-8 lp:p-10 md:gap-3 lg:gap-5 ${className}`} style={{ width: `${tamanho}%` }}>
            {children}
        </div>
    )
}

export function ConfLi({children}:ConfComp) {
    return (
        <li className="flex flex-col justify-between lg:text-[20px] lg:p-5">
            {children}
        </li>
    )
}

export function ConfNotificacoesText({children}:ConfComp) {
    return (
        <p className="font-poppins-sans md:text-[20px] lg:text-[24px] lp:text-[28px] pc:text-[32px]">
            {children}
        </p>
    )
}

export function ConfInfoLi({children}:ConfComp) {
    return (
        <li className="font-poppins-sans md:text-[20px] lp:text-[24px]">
            {children}
        </li>
    )
}